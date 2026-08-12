from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

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

router = APIRouter(
    prefix="/api/students",
    tags=["Students"],
)


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
            db.query(__import__(
                "app.models.user",
                fromlist=["User"]
            ).User)
            .filter(
                __import__(
                    "app.models.user",
                    fromlist=["User"]
                ).User.id == student.user_id
            )
            .first()
        )

        if user:
            result.append({
                "id": student.id,
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

    from app.models.user import User

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

    from app.models.user import User

    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    return {
        "id": student.id,
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