from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.substitution import Substitution
from app.schemas.substitution import SubstitutionCreate


def _get_leave(db: Session, institution_id: UUID, leave_id: UUID):
    return db.execute(
        text("SELECT * FROM leave_applications WHERE id = :lid AND institution_id = :iid"),
        {"lid": str(leave_id), "iid": str(institution_id)},
    ).mappings().first()


def _teachers_of_institution(db: Session, institution_id: UUID):
    return db.execute(
        text(
            "SELECT t.id AS teacher_id, t.user_id, u.full_name AS teacher_name "
            "FROM teachers t JOIN users u ON u.id = t.user_id "
            "WHERE t.institution_id = :iid"
        ),
        {"iid": str(institution_id)},
    ).mappings().all()


def _teacher_subject_ids(db: Session, teacher_id: UUID):
    return {
        row["subject_id"]
        for row in db.execute(
            text("SELECT subject_id FROM teacher_subjects WHERE teacher_id = :tid"),
            {"tid": str(teacher_id)},
        ).mappings().all()
    }


def suggest_substitutes(db: Session, institution_id: UUID, leave_application_id: UUID):
    leave = _get_leave(db, institution_id, leave_application_id)
    if not leave:
        raise ValueError("Leave application not found in this institution.")

    teacher_row = db.execute(
        text("SELECT id AS teacher_id FROM teachers WHERE user_id = :uid AND institution_id = :iid"),
        {"uid": str(leave["user_id"]), "iid": str(institution_id)},
    ).mappings().first()

    if not teacher_row:
        return []

    teacher_id = teacher_row["teacher_id"]

    schedule_rows = db.execute(
        text(
            "SELECT class_id, subject_id, day, period, subject_name FROM schedule_entries "
            "WHERE teacher_id = :tid AND institution_id = :iid"
        ),
        {"tid": str(teacher_id), "iid": str(institution_id)},
    ).mappings().all()

    if not schedule_rows:
        return []

    candidates = [
        t for t in _teachers_of_institution(db, institution_id) if t["teacher_id"] != teacher_id
    ]

    suggestions = []
    for entry in schedule_rows:
        if not entry["class_id"]:
            continue
        subject_ids = {str(entry["subject_id"])} if entry["subject_id"] else set()

        for cand in candidates:
            cand_subjects = _teacher_subject_ids(db, cand["teacher_id"])
            subject_match = bool(subject_ids and subject_ids & {str(s) for s in cand_subjects})

            busy = db.execute(
                text(
                    "SELECT 1 FROM schedule_entries WHERE teacher_id = :tid AND day = :day AND period = :p AND institution_id = :iid LIMIT 1"
                ),
                {
                    "tid": str(cand["teacher_id"]),
                    "day": entry["day"],
                    "p": entry["period"],
                    "iid": str(institution_id),
                },
            ).first()

            if busy:
                continue

            score = (2 if subject_match else 0) + 1
            class_row = db.execute(
                text("SELECT class_name FROM classes WHERE id = :cid"),
                {"cid": str(entry["class_id"])},
            ).mappings().first()

            suggestions.append(
                {
                    "leave_application_id": leave_application_id,
                    "teacher_id": teacher_id,
                    "substitute_teacher_id": cand["teacher_id"],
                    "substitute_name": cand["teacher_name"],
                    "class_id": entry["class_id"],
                    "class_name": class_row["class_name"] if class_row else None,
                    "subject_id": entry["subject_id"],
                    "subject_name": entry["subject_name"],
                    "day_of_week": entry["day"],
                    "period": entry["period"],
                    "score": score,
                    "reason": "Teaches same subject"
                    if subject_match
                    else "Available teacher (free period)",
                }
            )

    suggestions.sort(key=lambda s: (s["score"] or 0), reverse=True)
    return suggestions


def confirm_substitution(db: Session, institution_id: UUID, data: SubstitutionCreate, user_id: UUID):
    substitution = Substitution(
        institution_id=institution_id,
        leave_application_id=data.leave_application_id,
        teacher_id=data.teacher_id,
        substitute_teacher_id=data.substitute_teacher_id,
        class_id=data.class_id,
        subject_id=data.subject_id,
        day_of_week=data.day_of_week,
        period=data.period,
        status="confirmed",
        confirmed_by=user_id,
    )
    db.add(substitution)
    db.commit()
    db.refresh(substitution)
    return substitution


def list_substitutions(db: Session, institution_id: UUID, status: str | None = None):
    sql = """
        SELECT s.*,
               u1.full_name AS teacher_name,
               u2.full_name AS substitute_name,
               c.class_name,
               sub.subject_name,
               la.leave_type,
               la.start_date::text AS leave_start,
               la.end_date::text AS leave_end
        FROM substitutions s
        LEFT JOIN teachers t1 ON t1.id = s.teacher_id
        LEFT JOIN users u1 ON u1.id = t1.user_id
        LEFT JOIN teachers t2 ON t2.id = s.substitute_teacher_id
        LEFT JOIN users u2 ON u2.id = t2.user_id
        LEFT JOIN classes c ON c.id = s.class_id
        LEFT JOIN subjects sub ON sub.id = s.subject_id
        LEFT JOIN leave_applications la ON la.id = s.leave_application_id
        WHERE s.institution_id = :iid
    """
    params: dict = {"iid": str(institution_id)}
    if status:
        sql += " AND s.status = :status"
        params["status"] = status
    sql += " ORDER BY s.created_at DESC"
    return db.execute(text(sql), params).mappings().all()


def get_substitution(db: Session, institution_id: UUID, substitution_id: UUID):
    row = db.execute(
        text(
            "SELECT s.*, u2.full_name AS substitute_name, c.class_name, sub.subject_name "
            "FROM substitutions s "
            "LEFT JOIN teachers t2 ON t2.id = s.substitute_teacher_id "
            "LEFT JOIN users u2 ON u2.id = t2.user_id "
            "LEFT JOIN classes c ON c.id = s.class_id "
            "LEFT JOIN subjects sub ON sub.id = s.subject_id "
            "WHERE s.id = :sid AND s.institution_id = :iid"
        ),
        {"sid": str(substitution_id), "iid": str(institution_id)},
    ).mappings().first()
    return row


def delete_substitution(db: Session, institution_id: UUID, substitution_id: UUID):
    s = (
        db.query(Substitution)
        .filter(Substitution.id == substitution_id, Substitution.institution_id == institution_id)
        .first()
    )
    if not s:
        return None
    db.delete(s)
    db.commit()
    return s