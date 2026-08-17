"""Schedule / timetable service for PaperBuddy.

Reads real records from the existing Supabase tables (``classes``, ``subjects``,
``teachers``, ``rooms``, ``class_subjects``, ``teacher_subjects``) and stores
persistent timetable slots in the additive ``schedule_entries`` table.

The other tables are read defensively (``SELECT *`` + ``.get``) because their
exact columns are owned by the live database; ``schedule_entries`` is fully
described by the ORM model and the migration in ``docs/supabase_schedule_entries.sql``.
"""
from collections import defaultdict
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app.models.schedule import ScheduleEntry
from app.schemas.schedule import (
    ScheduleConflict,
    ScheduleEntryCreate,
    ScheduleEntryResponse,
    ScheduleEntryUpdate,
    ScheduleGenerateRequest,
)
from app.schemas.timetable import TimetableLesson
from app.services.timetable_service import solve_timetable


# ==========================================
# Defensive reads of existing database tables
# ==========================================
def _fetch_scoped_rows(db: Session, table: str, institution_id: str):
    """Return rows from a known table filtered to one institution.

    Uses ``WHERE institution_id`` first; if that column is absent the full
    result set is filtered in Python on the ``institution_id`` key. Rows are
    returned as dict-like mappings so missing keys can be detected.
    """
    try:
        rows = db.execute(
            text(f"SELECT * FROM {table} WHERE institution_id = :iid"),
            {"iid": str(institution_id)},
        ).mappings().all()
        return list(rows)
    except Exception:
        all_rows = db.execute(text(f"SELECT * FROM {table}")).mappings().all()
        return [
            row
            for row in all_rows
            if str(row.get("institution_id") or "") == str(institution_id)
        ]


def _get_subjects(db: Session, institution_id: str) -> list[dict]:
    rows = _fetch_scoped_rows(db, "subjects", institution_id)
    result = []
    for row in rows:
        result.append({
            "id": row["id"],
            "name": row.get("name") or row.get("subject_name") or f"Subject {str(row['id'])[:8]}",
            "code": row.get("code"),
        })
    return result


def _get_rooms(db: Session, institution_id: str) -> list[dict]:
    rows = _fetch_scoped_rows(db, "rooms", institution_id)
    result = []
    for row in rows:
        capacity = row.get("capacity")
        try:
            capacity = int(capacity) if capacity not in (None, "") else None
        except (TypeError, ValueError):
            capacity = None
        result.append({
            "id": row["id"],
            "name": row.get("name") or row.get("room_name") or f"Room {str(row['id'])[:8]}",
            "capacity": capacity,
        })
    return result


def _get_teachers(db: Session, institution_id: str) -> dict[str, dict]:
    rows = _fetch_scoped_rows(db, "teachers", institution_id)
    result: dict[str, dict] = {}
    user_ids = [str(row["user_id"]) for row in rows if row.get("user_id")]
    names_by_user: dict[str, str] = {}
    if user_ids:
        placeholders = ", ".join(f":uid_{i}" for i in range(len(user_ids)))
        params = {f"uid_{i}": uid for i, uid in enumerate(user_ids)}
        user_rows = db.execute(
            text(f"SELECT id, full_name FROM users WHERE id IN ({placeholders})"),
            params,
        ).mappings().all()
        names_by_user = {str(row["id"]): row["full_name"] for row in user_rows}
    for row in rows:
        teacher_id = str(row["id"])
        name = names_by_user.get(str(row.get("user_id") or ""))
        if not name:
            name = row.get("name") or row.get("full_name") or f"Teacher {teacher_id[:8]}"
        result[teacher_id] = {"id": teacher_id, "name": name}
    return result


def _get_class_subjects(db: Session, class_ids: set[str]) -> list[dict]:
    rows = db.execute(text("SELECT * FROM class_subjects")).mappings().all()
    return [
        {"class_id": row["class_id"], "subject_id": row["subject_id"]}
        for row in rows
        if str(row.get("class_id") or "") in class_ids and row.get("subject_id")
    ]


def _get_teacher_subjects(db: Session, teacher_ids: set[str]) -> list[dict]:
    rows = db.execute(text("SELECT * FROM teacher_subjects")).mappings().all()
    return [
        {"teacher_id": row["teacher_id"], "subject_id": row["subject_id"]}
        for row in rows
        if str(row.get("teacher_id") or "") in teacher_ids and row.get("subject_id")
    ]


# ==========================================
# Response helpers
# ==========================================
def _entry_to_response(db: Session, entry: ScheduleEntry) -> ScheduleEntryResponse:
    class_name = entry.class_name if hasattr(entry, "class_name") else None
    if class_name is None:
        class_row = db.execute(
            text("SELECT class_name, section FROM classes WHERE id = :cid"),
            {"cid": str(entry.class_id)},
        ).mappings().first()
        class_name = class_row["class_name"] if class_row else None
        section = class_row["section"] if class_row else None
    else:
        section = entry.section
    return ScheduleEntryResponse(
        id=entry.id,
        institution_id=entry.institution_id,
        class_id=entry.class_id,
        class_name=class_name,
        section=section,
        subject_id=entry.subject_id,
        subject_name=entry.subject_name,
        teacher_id=entry.teacher_id,
        teacher_name=entry.teacher_name,
        room_id=entry.room_id,
        room_name=entry.room_name,
        day=entry.day,
        period=entry.period,
        source=entry.source,
        created_at=entry.created_at,
        updated_at=entry.updated_at,
    )


def _slot_response(slot, institution_id: str | None = None) -> dict:
    return {
        "id": None,
        "institution_id": institution_id,
        "class_id": slot.class_id,
        "class_name": slot.class_name,
        "section": None,
        "subject_id": None,
        "subject_name": slot.subject,
        "teacher_id": slot.teacher_id,
        "teacher_name": slot.teacher_name,
        "room_id": None,
        "room_name": slot.room,
        "day": slot.day,
        "period": slot.period,
        "source": "generated",
    }


# ==========================================
# CRUD
# ==========================================
def _assert_class_in_institution(db: Session, class_id: UUID, institution_id: str):
    row = db.execute(
        text("SELECT id FROM classes WHERE id = :cid AND institution_id = :iid"),
        {"cid": str(class_id), "iid": institution_id},
    ).mappings().first()
    if not row:
        raise ValueError("The selected class does not belong to this institution.")


def create_schedule_entry(
    db: Session,
    institution_id: str,
    data: ScheduleEntryCreate,
) -> ScheduleEntryResponse:
    _assert_class_in_institution(db, data.class_id, institution_id)
    entry = ScheduleEntry(
        institution_id=institution_id,
        class_id=data.class_id,
        section=data.section,
        subject_id=data.subject_id,
        subject_name=data.subject_name,
        teacher_id=data.teacher_id,
        teacher_name=data.teacher_name,
        room_id=data.room_id,
        room_name=data.room_name,
        day=data.day,
        period=data.period,
        source="manual",
    )
    db.add(entry)
    try:
        db.commit()
        db.refresh(entry)
    except IntegrityError:
        db.rollback()
        raise ValueError(
            "This entry conflicts with an existing schedule entry (same class/teacher/room on the same day and period)."
        )
    return _entry_to_response(db, entry)


def update_schedule_entry(
    db: Session,
    institution_id: str,
    entry_id: UUID,
    data: ScheduleEntryUpdate,
) -> ScheduleEntryResponse:
    entry = (
        db.query(ScheduleEntry)
        .filter(
            ScheduleEntry.id == entry_id,
            ScheduleEntry.institution_id == institution_id,
        )
        .first()
    )
    if not entry:
        raise ValueError("Schedule entry not found.")
    fields = data.model_dump(exclude_unset=True)
    if "class_id" in fields and fields["class_id"] is not None:
        _assert_class_in_institution(db, fields["class_id"], institution_id)
    for key, value in fields.items():
        setattr(entry, key, value)
    db.commit()
    db.refresh(entry)
    return _entry_to_response(db, entry)


def delete_schedule_entry(
    db: Session,
    institution_id: str,
    entry_id: UUID,
) -> bool:
    entry = (
        db.query(ScheduleEntry)
        .filter(
            ScheduleEntry.id == entry_id,
            ScheduleEntry.institution_id == institution_id,
        )
        .first()
    )
    if not entry:
        return False
    db.delete(entry)
    db.commit()
    return True


def list_schedule_entries(
    db: Session,
    institution_id: str,
    class_id: UUID | None = None,
    teacher_id: UUID | None = None,
    day: str | None = None,
) -> list[ScheduleEntryResponse]:
    query = db.query(ScheduleEntry).filter(
        ScheduleEntry.institution_id == institution_id
    )
    if class_id is not None:
        query = query.filter(ScheduleEntry.class_id == class_id)
    if teacher_id is not None:
        query = query.filter(ScheduleEntry.teacher_id == teacher_id)
    if day is not None:
        query = query.filter(ScheduleEntry.day == day)
    entries = query.order_by(ScheduleEntry.day, ScheduleEntry.period).all()
    return [_entry_to_response(db, entry) for entry in entries]


# ==========================================
# Conflict detection
# ==========================================
def detect_conflicts(
    db: Session,
    institution_id: str,
) -> list[ScheduleConflict]:
    entries = (
        db.query(ScheduleEntry)
        .filter(ScheduleEntry.institution_id == institution_id)
        .all()
    )
    groups: dict[str, list[ScheduleEntry]] = defaultdict(list)
    for entry in entries:
        for kind, value in (
            ("teacher", entry.teacher_id),
            ("class", entry.class_id),
            ("room", entry.room_id),
        ):
            if value is not None:
                groups[f"{kind}|{value}|{entry.day}|{entry.period}"].append(entry)

    conflicts: list[ScheduleConflict] = []
    for key, group_entries in groups.items():
        if len(group_entries) < 2:
            continue
        kind = key.split("|")[0]
        first = group_entries[0]
        if kind == "teacher":
            label = first.teacher_name or str(first.teacher_id)[:8]
        elif kind == "class":
            label = f"class {str(first.class_id)[:8]}"
        else:
            label = first.room_name or str(first.room_id)[:8]
        conflicts.append(
            ScheduleConflict(
                type=kind,
                day=first.day,
                period=first.period,
                value=label,
                entries=[entry.id for entry in group_entries],
            )
        )
    return conflicts


def list_classes(db: Session, institution_id: str) -> list[dict]:
    rows = db.execute(
        text("SELECT id, class_name, section FROM classes WHERE institution_id = :iid ORDER BY class_name"),
        {"iid": str(institution_id)},
    ).mappings().all()
    return [{"id": row["id"], "name": row["class_name"], "section": row.get("section")} for row in rows]


def list_teachers(db: Session, institution_id: str) -> list[dict]:
    teachers = _get_teachers(db, institution_id)
    return [
        {"id": teacher["id"], "name": teacher["name"]}
        for teacher in sorted(teachers.values(), key=lambda item: item["name"].lower())
    ]


def list_subjects(db: Session, institution_id: str) -> list[dict]:
    subjects = _get_subjects(db, institution_id)
    return [
        {"id": subject["id"], "name": subject["name"]}
        for subject in sorted(subjects, key=lambda item: item["name"].lower())
    ]


# ==========================================
# OR-Tools generation from real database records
# ==========================================
def generate_schedule(
    db: Session,
    institution_id: str,
    request: ScheduleGenerateRequest,
) -> dict:
    class_query = db.execute(
        text(
            "SELECT id, class_name, section FROM classes WHERE institution_id = :iid"
            + (" AND id = ANY(:class_ids)" if request.class_ids else "")
        ),
        {
            "iid": str(institution_id),
            **(
                {"class_ids": [str(cid) for cid in request.class_ids]}
                if request.class_ids
                else {}
            ),
        },
    ).mappings().all()
    classes = [dict(row) for row in class_query]
    if not classes:
        raise ValueError("No classes found for this institution.")

    subjects = {str(sub["id"]): sub for sub in _get_subjects(db, institution_id)}
    teachers = _get_teachers(db, institution_id)
    rooms = _get_rooms(db, institution_id)

    class_ids = {str(cls["id"]) for cls in classes}
    class_subject_pairs = _get_class_subjects(db, class_ids)
    teacher_subject_pairs = _get_teacher_subjects(db, set(teachers.keys()))

    subjects_by_class: dict[str, list[str]] = defaultdict(list)
    for pair in class_subject_pairs:
        subjects_by_class[str(pair["class_id"])].append(str(pair["subject_id"]))
    teachers_by_subject: dict[str, list[str]] = defaultdict(list)
    for pair in teacher_subject_pairs:
        teachers_by_subject[str(pair["subject_id"])].append(str(pair["teacher_id"]))

    rooms_by_class: dict[str, dict] = {}
    if rooms:
        for index, cls in enumerate(classes):
            rooms_by_class[str(cls["id"])] = rooms[index % len(rooms)]

    lessons: list[TimetableLesson] = []
    skipped: list[dict] = []
    for cls in classes:
        class_label = cls["class_name"] + (f" {cls['section']}" if cls.get("section") else "")
        subject_ids = subjects_by_class.get(str(cls["id"]), [])
        if not subject_ids:
            skipped.append({
                "class": class_label,
                "subject": None,
                "reason": "No subjects are assigned to this class.",
            })
            continue
        room = rooms_by_class.get(str(cls["id"]))
        for subject_id in subject_ids:
            subject = subjects.get(subject_id)
            if not subject:
                continue
            qualified = teachers_by_subject.get(subject_id, [])
            teacher = teachers.get(qualified[0]) if qualified else None
            if not teacher:
                skipped.append({
                    "class": class_label,
                    "subject": subject["name"],
                    "reason": "No teacher is assigned to this subject.",
                })
                continue
            lessons.append(
                TimetableLesson(
                    teacher_id=teacher["id"],
                    teacher_name=teacher["name"],
                    class_id=str(cls["id"]),
                    class_name=class_label,
                    subject=subject["name"],
                    room=room["name"] if room else "",
                    sessions_per_week=request.sessions_per_week,
                )
            )

    if not lessons:
        raise ValueError(
            "No schedulable lessons were found from real database records. "
            "Assign subjects to classes and teachers to subjects first."
        )

    slots = solve_timetable(lessons, request.working_days, request.periods_per_day)

    generated: list[ScheduleEntryResponse] = []
    if request.persist:
        db.execute(
            text(
                "DELETE FROM schedule_entries "
                "WHERE institution_id = :iid AND source = 'generated'"
            ),
            {"iid": str(institution_id)},
        )
        for slot in slots:
            entry = ScheduleEntry(
                institution_id=institution_id,
                class_id=slot.class_id,
                section=None,
                subject_name=slot.subject,
                teacher_id=slot.teacher_id,
                teacher_name=slot.teacher_name,
                room_name=slot.room or None,
                day=slot.day,
                period=slot.period,
                source="generated",
            )
            db.add(entry)
        db.commit()
        for slot in slots:
            entry = (
                db.query(ScheduleEntry)
                .filter(
                    ScheduleEntry.institution_id == institution_id,
                    ScheduleEntry.class_id == slot.class_id,
                    ScheduleEntry.day == slot.day,
                    ScheduleEntry.period == slot.period,
                    ScheduleEntry.source == "generated",
                    ScheduleEntry.subject_name == slot.subject,
                )
                .first()
            )
            generated.append(_entry_to_response(db, entry) if entry else _slot_response(slot, institution_id))
    else:
        generated = [
            ScheduleEntryResponse(**_slot_response(slot, institution_id))
            for slot in slots
        ]

    conflicts = detect_conflicts(db, institution_id)

    return {
        "status": "success",
        "message": (
            f"Generated {len(generated)} timetable slots for {len(classes)} class(es)."
        ),
        "generated": generated,
        "skipped": skipped,
        "conflicts": len(conflicts),
    }