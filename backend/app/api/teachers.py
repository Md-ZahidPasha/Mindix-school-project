from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.schemas.teacher import (
    TeacherCreate,
    TeacherUpdate,
    TeacherResponse,
)
from app.services.teacher_service import (
    create_teacher,
    get_teachers,
    get_teacher,
    get_teacher_by_user,
    update_teacher,
    delete_teacher,
    get_teacher_dashboard,
    get_teacher_classes,
    get_teacher_students,
    get_teacher_subject_ids,
)
from app.models.user import User


router = APIRouter(
    prefix="/api/teachers",
    tags=["Teachers"],
)

security = HTTPBearer()

STAFF_MANAGER_ROLES = {"admin", "principal", "staff"}


def require_teacher(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
        )
    role = (user.get("role") or "").lower()
    if role not in {"admin", "principal", "teacher", "staff"}:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="A school staff/teacher account is required.",
        )
    if not user.get("institution_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing the institution scope.",
        )
    return user


def require_teacher_manager(
    credentials: HTTPAuthorizationCredentials = Depends(security),
):
    user = require_teacher(credentials)
    if (user.get("role") or "").lower() not in STAFF_MANAGER_ROLES:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admin, principal or staff can manage teachers.",
        )
    return user


def _resolve_teacher(db: Session, user: dict) -> tuple:
    """Return the Teacher row for a logged-in teacher, raising 403 for admins."""
    role = (user.get("role") or "").lower()
    institution_id = user["institution_id"]

    teacher = get_teacher_by_user(db, user.get("user_id"), institution_id)
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher profile not found for this account.",
        )
    return teacher, institution_id


# ==========================================
# My profile (authenticated teacher)
# ==========================================
@router.get("/me")
def teacher_me(
    current_user: dict = Depends(require_teacher),
    db: Session = Depends(get_db),
):
    role = (current_user.get("role") or "").lower()
    if role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access the teacher profile.",
        )
    teacher, institution_id = _resolve_teacher(db, current_user)
    user = (
        db.query(User)
        .filter(User.id == teacher.user_id)
        .first()
    )
    return {
        "id": str(teacher.id),
        "user_id": str(teacher.user_id),
        "full_name": user.full_name if user else None,
        "email": user.email if user else None,
        "phone": user.phone if user else None,
        "department_id": str(teacher.department_id) if teacher.department_id else None,
        "qualification": teacher.qualification,
        "specialization": teacher.specialization,
        "joining_date": teacher.joining_date,
        "institution_id": str(teacher.institution_id) if teacher.institution_id else None,
        "subject_ids": [str(s) for s in get_teacher_subject_ids(db, teacher.id)],
    }


# ==========================================
# My dashboard (authenticated teacher)
# ==========================================
@router.get("/me/dashboard")
def teacher_dashboard(
    current_user: dict = Depends(require_teacher),
    db: Session = Depends(get_db),
):
    role = (current_user.get("role") or "").lower()
    if role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access the teacher dashboard.",
        )
    teacher, institution_id = _resolve_teacher(db, current_user)
    dashboard = get_teacher_dashboard(db, teacher.id, institution_id)
    return dashboard


# ==========================================
# My classes (authenticated teacher)
# ==========================================
@router.get("/me/classes")
def teacher_classes(
    current_user: dict = Depends(require_teacher),
    db: Session = Depends(get_db),
):
    role = (current_user.get("role") or "").lower()
    if role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access teacher classes.",
        )
    teacher, institution_id = _resolve_teacher(db, current_user)
    return get_teacher_classes(db, teacher.id, institution_id)


# ==========================================
# My students (authenticated teacher)
# ==========================================
@router.get("/me/students")
def teacher_students(
    current_user: dict = Depends(require_teacher),
    db: Session = Depends(get_db),
):
    role = (current_user.get("role") or "").lower()
    if role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access teacher students.",
        )
    teacher, institution_id = _resolve_teacher(db, current_user)
    return get_teacher_students(db, teacher.id, institution_id)


# ==========================================
# My timetable (authenticated teacher)
# ==========================================
@router.get("/me/timetable")
def teacher_timetable(
    current_user: dict = Depends(require_teacher),
    db: Session = Depends(get_db),
):
    role = (current_user.get("role") or "").lower()
    if role != "teacher":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only teachers can access teacher timetable.",
        )
    teacher, institution_id = _resolve_teacher(db, current_user)
    rows = db.execute(
        text(
            "SELECT se.day, se.period, se.subject_name, "
            "CASE WHEN c.class_name IS NULL THEN 'Class' ELSE c.class_name END AS class_name, "
            "c.section, se.room_name "
            "FROM schedule_entries se "
            "LEFT JOIN classes c ON c.id = se.class_id "
            "WHERE se.teacher_id = :tid AND se.institution_id = :iid "
            "ORDER BY se.day, se.period"
        ),
        {"tid": str(teacher.id), "iid": str(institution_id)},
    ).mappings().all()
    return [
        {
            "day": row["day"],
            "period": row["period"],
            "subject": row["subject_name"],
            "class_name": row["class_name"],
            "section": row["section"],
            "room": row["room_name"],
        }
        for row in rows
    ]


# ==========================================
# Create Teacher (admin / principal / staff)
# ==========================================
@router.post(
    "",
    response_model=TeacherResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_teacher_endpoint(
    teacher_data: TeacherCreate,
    current_user: dict = Depends(require_teacher_manager),
    db: Session = Depends(get_db),
):
    try:
        teacher, user = create_teacher(db, teacher_data)
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
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# List Teachers (admin / principal / staff)
# ==========================================
@router.get(
    "",
    response_model=list[TeacherResponse],
)
def list_teachers_endpoint(
    institution_id: UUID = Query(...),
    current_user: dict = Depends(require_teacher_manager),
    db: Session = Depends(get_db),
):
    teachers = get_teachers(db, institution_id)
    result = []
    for teacher in teachers:
        user = (
            db.query(User)
            .filter(User.id == teacher.user_id)
            .first()
        )
        if not user:
            continue
        result.append({
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
        })
    return result


# ==========================================
# Get One Teacher (admin / principal / staff)
# ==========================================
@router.get(
    "/{teacher_id}",
    response_model=TeacherResponse,
)
def get_teacher_endpoint(
    teacher_id: UUID,
    institution_id: UUID = Query(...),
    current_user: dict = Depends(require_teacher_manager),
    db: Session = Depends(get_db),
):
    teacher = get_teacher(db, teacher_id, institution_id)
    if not teacher:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found",
        )
    user = (
        db.query(User)
        .filter(User.id == teacher.user_id)
        .first()
    )
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher user account not found",
        )
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
# Update Teacher (admin / principal / staff)
# ==========================================
@router.put(
    "/{teacher_id}",
    response_model=TeacherResponse,
)
def update_teacher_endpoint(
    teacher_id: UUID,
    teacher_data: TeacherUpdate,
    institution_id: UUID = Query(...),
    current_user: dict = Depends(require_teacher_manager),
    db: Session = Depends(get_db),
):
    try:
        teacher = update_teacher(db, teacher_id, institution_id, teacher_data)
        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )
        user = (
            db.query(User)
            .filter(User.id == teacher.user_id)
            .first()
        )
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher user account not found",
            )
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
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# Delete Teacher (admin / principal / staff)
# ==========================================
@router.delete(
    "/{teacher_id}",
)
def delete_teacher_endpoint(
    teacher_id: UUID,
    institution_id: UUID = Query(...),
    current_user: dict = Depends(require_teacher_manager),
    db: Session = Depends(get_db),
):
    deleted = delete_teacher(db, teacher_id, institution_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Teacher not found",
        )
    return {
        "status": "success",
        "message": "Teacher deleted successfully",
    }