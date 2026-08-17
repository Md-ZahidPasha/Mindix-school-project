from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.schemas.student import (
    StudentCreate,
    StudentUpdate,
    StudentResponse,
)
from app.services.student_service import (
    create_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)
from app.models.user import User
from app.models.student import Student


router = APIRouter(
    prefix="/api/students",
    tags=["Students"],
)

security = HTTPBearer()


def require_student(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
        )
    if (user.get("role") or "").lower() != "student":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="A student account is required.",
        )
    if not user.get("institution_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing the institution scope.",
        )
    return user


@router.get("/me")
def student_me(
    current_user: dict = Depends(require_student),
    db: Session = Depends(get_db),
):
    student = (
        db.query(Student)
        .filter(
            Student.student_id == current_user.get("student_id"),
            Student.institution_id == current_user.get("institution_id"),
        )
        .first()
    )
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student profile not found.",
        )
    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )
    class_row = (
        db.execute(
            text("SELECT class_name, section FROM classes WHERE id = :cid"),
            {"cid": str(student.class_id)},
        ).mappings().first()
        if student.class_id
        else None
    )
    return {
        "id": str(student.id),
        "student_id": student.student_id,
        "full_name": user.full_name if user else None,
        "email": user.email if user else None,
        "phone": user.phone if user else None,
        "roll_number": student.roll_number,
        "admission_number": student.admission_number,
        "date_of_birth": student.date_of_birth,
        "gender": student.gender,
        "class_id": str(student.class_id) if student.class_id else None,
        "class_name": class_row["class_name"] if class_row else None,
        "section": class_row["section"] if class_row else None,
        "institution_id": str(student.institution_id) if student.institution_id else None,
    }


@router.get("/dashboard")
def student_dashboard(
    current_user: dict = Depends(require_student),
    db: Session = Depends(get_db),
):
    me = student_me(current_user, db)

    attendance_rows = db.execute(
        text(
            "SELECT status, COUNT(*) AS count FROM attendance "
            "WHERE student_id = :sid AND institution_id = :iid "
            "GROUP BY status"
        ),
        {"sid": me["id"], "iid": me["institution_id"]},
    ).mappings().all()

    present = 0
    absent = 0
    for row in attendance_rows:
        status_value = (row["status"] or "").lower()
        if status_value == "present":
            present += int(row["count"])
        elif status_value in {"absent", "leave"}:
            absent += int(row["count"])
    total = present + absent
    percentage = round(present / total * 100, 1) if total else 0

    recent_rows = db.execute(
        text(
            "SELECT attendance_date, status FROM attendance "
            "WHERE student_id = :sid AND institution_id = :iid "
            "ORDER BY attendance_date DESC LIMIT 20"
        ),
        {"sid": me["id"], "iid": me["institution_id"]},
    ).mappings().all()
    recent_attendance = [
        {
            "date": str(row["attendance_date"]),
            "status": (row["status"] or "present").capitalize(),
        }
        for row in recent_rows
    ]

    slots = []
    if me.get("class_id"):
        rows = db.execute(
            text(
                "SELECT day, period, subject_name, teacher_name, room_name "
                "FROM schedule_entries WHERE class_id = :cid "
                "ORDER BY day, period"
            ),
            {"cid": me["class_id"]},
        ).mappings().all()
        for row in rows:
            slots.append({
                "day": row["day"],
                "period": row["period"],
                "subject": row["subject_name"],
                "teacher": row["teacher_name"] or "Teacher",
                "room": row["room_name"] or None,
            })

    return {
        "student": {
            "name": me["full_name"],
            "class": me["class_name"],
            "section": me["section"],
            "roll_number": me["roll_number"],
            "student_id": me["student_id"],
        },
        "attendance": {
            "percentage": percentage,
            "present": present,
            "absent": absent,
            "late": 0,
            "upcoming": 0,
            "pending": 0,
        },
        "recent_attendance": recent_attendance,
        "timetable": {"slots": slots},
    }


@router.post(
    "",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_student_endpoint(
    student_data: StudentCreate,
    db: Session = Depends(get_db),
):
    try:
        student, user = create_student(
            db,
            student_data
        )

        return {
            "id": student.id,
            "student_id": student.student_id,
            "user_id": student.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "roll_number": student.roll_number,
            "admission_number": student.admission_number,
            "date_of_birth": student.date_of_birth,
            "gender": student.gender,
            "class_id": student.class_id,
            "institution_id": student.institution_id,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.get(
    "",
    response_model=list[StudentResponse],
)
def list_students(
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    students = get_students(
        db,
        institution_id
    )

    result = []

    for student in students:
        user = (
            db.query(User)
            .filter(User.id == student.user_id)
            .first()
        )

        if user:
            result.append({
                "id": student.id,
                "student_id": student.student_id,
                "user_id": student.user_id,
                "full_name": user.full_name,
                "email": user.email,
                "phone": user.phone,
                "roll_number": student.roll_number,
                "admission_number": student.admission_number,
                "date_of_birth": student.date_of_birth,
                "gender": student.gender,
                "class_id": student.class_id,
                "institution_id": student.institution_id,
            })

    return result


@router.get(
    "/{student_id}",
    response_model=StudentResponse,
)
def get_student_endpoint(
    student_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    student = get_student(
        db,
        student_id,
        institution_id
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student user account not found",
        )

    return {
        "id": student.id,
        "student_id": student.student_id,
        "user_id": student.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "roll_number": student.roll_number,
        "admission_number": student.admission_number,
        "date_of_birth": student.date_of_birth,
        "gender": student.gender,
        "class_id": student.class_id,
        "institution_id": student.institution_id,
    }


@router.put(
    "/{student_id}",
    response_model=StudentResponse,
)
def update_student_endpoint(
    student_id: UUID,
    student_data: StudentUpdate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    student = update_student(
        db,
        student_id,
        institution_id,
        student_data
    )

    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student user account not found",
        )

    return {
        "id": student.id,
        "student_id": student.student_id,
        "user_id": student.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "roll_number": student.roll_number,
        "admission_number": student.admission_number,
        "date_of_birth": student.date_of_birth,
        "gender": student.gender,
        "class_id": student.class_id,
        "institution_id": student.institution_id,
    }


@router.delete(
    "/{student_id}",
)
def delete_student_endpoint(
    student_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_student(
        db,
        student_id,
        institution_id
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )

    return {
        "status": "success",
        "message": "Student deleted successfully",
    }