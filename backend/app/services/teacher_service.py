from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.teacher import Teacher
from app.models.teacher_subject import TeacherSubject
from app.models.user import User
from app.schemas.teacher import TeacherCreate, TeacherUpdate
from app.core.security import hash_password


# ==========================================
# Get Teacher by user_id
# ==========================================
def get_teacher_by_user(
    db: Session,
    user_id: UUID,
    institution_id: UUID,
):
    return (
        db.query(Teacher)
        .filter(
            Teacher.user_id == user_id,
            Teacher.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Get Teacher by id
# ==========================================
def get_teacher(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
):
    return (
        db.query(Teacher)
        .filter(
            Teacher.id == teacher_id,
            Teacher.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Teacher subjects
# ==========================================
def get_teacher_subject_ids(
    db: Session,
    teacher_id: UUID,
) -> list[UUID]:
    rows = (
        db.query(TeacherSubject.subject_id)
        .filter(TeacherSubject.teacher_id == teacher_id)
        .all()
    )
    return [row[0] for row in rows]


def set_teacher_subjects(
    db: Session,
    teacher_id: UUID,
    subject_ids: list[UUID],
    institution_id: UUID,
):
    db.query(TeacherSubject).filter(
        TeacherSubject.teacher_id == teacher_id
    ).delete()

    for subject_id in subject_ids:
        db.add(
            TeacherSubject(
                teacher_id=teacher_id,
                subject_id=subject_id,
                institution_id=institution_id,
            )
        )
    db.flush()


# ==========================================
# Build response payload
# ==========================================
def _teacher_response(db: Session, teacher: Teacher, user: User) -> dict:
    return {
        "id": teacher.id,
        "user_id": teacher.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "department_id": teacher.department_id,
        "qualification": teacher.qualification,
        "specialization": teacher.specialization,
        "joining_date": teacher.joining_date,
        "institution_id": teacher.institution_id,
        "subject_ids": get_teacher_subject_ids(db, teacher.id),
    }


# ==========================================
# Create Teacher
# ==========================================
def create_teacher(
    db: Session,
    teacher_data: TeacherCreate,
):
    existing_user = (
        db.query(User)
        .filter(User.email == teacher_data.email)
        .first()
    )

    if existing_user:
        raise ValueError("A user with this email already exists")

    user = User(
        institution_id=teacher_data.institution_id,
        full_name=teacher_data.full_name,
        email=teacher_data.email,
        phone=teacher_data.phone,
        password_hash=hash_password(teacher_data.password),
        role="teacher",
        status="active",
    )

    db.add(user)
    db.flush()

    teacher = Teacher(
        user_id=user.id,
        institution_id=teacher_data.institution_id,
        department_id=teacher_data.department_id,
        qualification=teacher_data.qualification,
        specialization=teacher_data.specialization,
        joining_date=teacher_data.joining_date,
    )

    db.add(teacher)
    db.flush()

    if teacher_data.subject_ids:
        set_teacher_subjects(
            db,
            teacher.id,
            teacher_data.subject_ids,
            teacher_data.institution_id,
        )

    db.commit()
    db.refresh(teacher)
    db.refresh(user)

    return teacher, user


# ==========================================
# List Teachers
# ==========================================
def get_teachers(
    db: Session,
    institution_id: UUID,
):
    return (
        db.query(Teacher)
        .filter(Teacher.institution_id == institution_id)
        .all()
    )


# ==========================================
# Update Teacher
# ==========================================
def update_teacher(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
    teacher_data: TeacherUpdate,
):
    teacher = get_teacher(db, teacher_id, institution_id)

    if not teacher:
        return None

    user = (
        db.query(User)
        .filter(User.id == teacher.user_id)
        .first()
    )

    data = teacher_data.model_dump(exclude_unset=True)

    if "email" in data and user:
        existing_user = (
            db.query(User)
            .filter(
                User.email == data["email"],
                User.id != user.id,
            )
            .first()
        )
        if existing_user:
            raise ValueError("A user with this email already exists")

    if user:
        if "full_name" in data:
            user.full_name = data["full_name"]
        if "email" in data:
            user.email = data["email"]
        if "phone" in data:
            user.phone = data["phone"]
        if "password" in data and data["password"]:
            user.password_hash = hash_password(data["password"])

    teacher_fields = [
        "department_id",
        "qualification",
        "specialization",
        "joining_date",
    ]

    for field in teacher_fields:
        if field in data:
            setattr(teacher, field, data[field])

    if "subject_ids" in data and data["subject_ids"] is not None:
        set_teacher_subjects(
            db,
            teacher.id,
            data["subject_ids"],
            institution_id,
        )

    db.commit()
    db.refresh(teacher)

    return teacher


# ==========================================
# Delete Teacher
# ==========================================
def delete_teacher(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
):
    teacher = get_teacher(db, teacher_id, institution_id)

    if not teacher:
        return None

    user = (
        db.query(User)
        .filter(User.id == teacher.user_id)
        .first()
    )

    db.query(TeacherSubject).filter(
        TeacherSubject.teacher_id == teacher.id
    ).delete()

    db.delete(teacher)

    if user:
        db.delete(user)

    db.commit()

    return True


# ==========================================
# Teacher dashboard / classes / students
# ==========================================
def get_teacher_classes(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
) -> list[dict]:
    """Classes this teacher is assigned to, via subject assignment + timetable."""
    subject_ids = get_teacher_subject_ids(db, teacher_id)

    # Prefer classes actually present in the generated timetable for this teacher.
    schedule_rows = db.execute(
        text(
            "SELECT DISTINCT class_id, section FROM schedule_entries "
            "WHERE teacher_id = :tid AND institution_id = :iid AND class_id IS NOT NULL"
        ),
        {"tid": str(teacher_id), "iid": str(institution_id)},
    ).mappings().all()

    class_ids = {str(row["class_id"]) for row in schedule_rows}
    section_map = {str(row["class_id"]): row["section"] for row in schedule_rows}

    if subject_ids and not class_ids:
        placeholders = ", ".join(f":sid_{i}" for i in range(len(subject_ids)))
        rows = db.execute(
            text(
                f"SELECT DISTINCT cs.class_id FROM class_subjects cs "
                f"WHERE cs.subject_id IN ({placeholders}) AND cs.institution_id = :iid"
            ),
            {
                **{f"sid_{i}": str(s) for i, s in enumerate(subject_ids)},
                "iid": str(institution_id),
            },
        ).mappings().all()
        class_ids = {str(row["class_id"]) for row in rows}

    if not class_ids:
        return []

    placeholders = ", ".join(f":cid_{i}" for i in range(len(class_ids)))
    params = {f"cid_{i}": cid for i, cid in enumerate(class_ids)}
    class_rows = db.execute(
        text(
            f"SELECT id, class_name, section FROM classes "
            f"WHERE institution_id = :iid AND id IN ({placeholders}) ORDER BY class_name"
        ),
        {**params, "iid": str(institution_id)},
    ).mappings().all()

    result = []
    for row in class_rows:
        cid = str(row["id"])
        student_count = db.execute(
            text("SELECT COUNT(*) FROM students WHERE class_id = :cid"),
            {"cid": cid},
        ).scalar() or 0
        result.append({
            "id": cid,
            "class_name": row["class_name"],
            "section": section_map.get(cid) or row["section"],
            "student_count": int(student_count),
        })
    return result


def get_teacher_students(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
) -> list[dict]:
    classes = get_teacher_classes(db, teacher_id, institution_id)
    if not classes:
        return []

    class_ids = [cls["id"] for cls in classes]
    placeholders = ", ".join(f":cid_{i}" for i in range(len(class_ids)))
    rows = db.execute(
        text(
            f"SELECT s.id, s.student_id, s.roll_number, s.class_id, "
            f"u.full_name, u.email, c.class_name, c.section "
            f"FROM students s "
            f"JOIN users u ON u.id = s.user_id "
            f"LEFT JOIN classes c ON c.id = s.class_id "
            f"WHERE s.class_id IN ({placeholders}) "
            f"ORDER BY c.class_name, u.full_name"
        ),
        {f"cid_{i}": cid for i, cid in enumerate(class_ids)},
    ).mappings().all()

    return [
        {
            "id": str(row["id"]),
            "student_id": row["student_id"],
            "roll_number": row["roll_number"],
            "full_name": row["full_name"],
            "email": row["email"],
            "class_id": str(row["class_id"]) if row["class_id"] else None,
            "class_name": row["class_name"],
            "section": row["section"],
        }
        for row in rows
    ]


def get_teacher_dashboard(
    db: Session,
    teacher_id: UUID,
    institution_id: UUID,
) -> dict:
    teacher = get_teacher(db, teacher_id, institution_id)
    if not teacher:
        return None

    user = (
        db.query(User)
        .filter(User.id == teacher.user_id)
        .first()
    )

    classes = get_teacher_classes(db, teacher_id, institution_id)
    students = get_teacher_students(db, teacher_id, institution_id)

    # Today's schedule
    today = db.execute(
        text("SELECT TO_CHAR(CURRENT_DATE, 'FMDay')")
    ).scalar()

    today_slots = db.execute(
        text(
            "SELECT day, period, subject_name, class_id, room_name, "
            "CASE WHEN c.class_name IS NULL THEN 'Class' ELSE c.class_name END AS class_name, c.section "
            "FROM schedule_entries se "
            "LEFT JOIN classes c ON c.id = se.class_id "
            "WHERE se.teacher_id = :tid AND se.institution_id = :iid AND LOWER(se.day) = LOWER(:day) "
            "ORDER BY se.period"
        ),
        {"tid": str(teacher_id), "iid": str(institution_id), "day": today},
    ).mappings().all()

    # Attendance summary (for this teacher's class ids)
    student_ids = [s["id"] for s in students]
    attendance = {"percentage": 0, "present": 0, "absent": 0, "total": 0}
    if student_ids:
        placeholders = ", ".join(f":sid_{i}" for i in range(len(student_ids)))
        att_rows = db.execute(
            text(
                f"SELECT status, COUNT(*) AS cnt FROM attendance "
                f"WHERE student_id IN ({placeholders}) GROUP BY status"
            ),
            {f"sid_{i}": sid for i, sid in enumerate(student_ids)},
        ).mappings().all()
        present = absent = 0
        for row in att_rows:
            s = (row["status"] or "").lower()
            if s == "present":
                present += int(row["cnt"])
            elif s in {"absent", "leave"}:
                absent += int(row["cnt"])
        total = present + absent
        attendance = {
            "percentage": round(present / total * 100, 1) if total else 0,
            "present": present,
            "absent": absent,
            "total": total,
        }

    # Leave requests for this teacher's user
    leaves = db.execute(
        text(
            "SELECT id, leave_type, start_date, end_date, status FROM leave_applications "
            "WHERE user_id = :uid AND institution_id = :iid ORDER BY created_at DESC LIMIT 10"
        ),
        {"uid": str(teacher.user_id), "iid": str(institution_id)},
    ).mappings().all()

    return {
        "teacher": {
            "id": str(teacher.id),
            "user_id": str(teacher.user_id),
            "full_name": user.full_name if user else "Teacher",
            "email": user.email if user else None,
            "phone": user.phone if user else None,
            "qualification": teacher.qualification,
            "specialization": teacher.specialization,
            "joining_date": teacher.joining_date,
        },
        "stats": {
            "classes": len(classes),
            "students": len(students),
            "today_classes": len(today_slots),
        },
        "today_schedule": [
            {
                "period": row["period"],
                "subject": row["subject_name"],
                "class_name": row["class_name"],
                "section": row["section"],
                "room": row["room_name"],
            }
            for row in today_slots
        ],
        "attendance": attendance,
        "leave_requests": [
            {
                "id": str(row["id"]),
                "leave_type": row["leave_type"],
                "start_date": str(row["start_date"]),
                "end_date": str(row["end_date"]),
                "status": row["status"],
            }
            for row in leaves
        ],
    }