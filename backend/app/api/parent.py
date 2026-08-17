from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.user import User

from app.schemas.parent import (
    ParentCreate,
    ParentUpdate,
    ParentResponse,
    ParentStudentCreate,
    ParentStudentResponse,
)

from app.services.parent_service import (
    create_parent,
    get_parents,
    get_parent,
    get_parent_user,
    get_parent_students,
    get_parent_by_parent_id,
    update_parent,
    delete_parent,
    add_student_to_parent,
    get_students_of_parent,
    remove_student_from_parent,
)


router = APIRouter(
    prefix="/api/parents",
    tags=["Parents"],
)


security = HTTPBearer()


def _require_parent(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    payload = decode_access_token(credentials.credentials)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if (payload.get("role") or "").lower() != "parent":
        raise HTTPException(status_code=403, detail="Parent authorization is required.")
    if not payload.get("parent_id") or not payload.get("institution_id"):
        raise HTTPException(status_code=401, detail="Token is missing the parent scope.")
    return payload


# ==========================================
# Parent Profile (me)
# ==========================================
@router.get("/me")
def parent_me(
    current_parent: dict = Depends(_require_parent),
    db: Session = Depends(get_db),
):
    parent = get_parent_by_parent_id(
        db,
        current_parent["parent_id"],
        UUID(current_parent["institution_id"]),
    )
    if not parent:
        raise HTTPException(status_code=404, detail="Parent profile not found.")
    user = get_parent_user(db, parent)
    return {
        "parent_id": parent.parent_id,
        "user_id": str(parent.user_id),
        "institution_id": str(parent.institution_id),
        "full_name": user.full_name if user else None,
        "email": user.email if user else None,
        "phone": user.phone if user else parent.phone,
    }


@router.get("/me/children")
def parent_children(
    current_parent: dict = Depends(_require_parent),
    db: Session = Depends(get_db),
):
    parent = get_parent_by_parent_id(
        db,
        current_parent["parent_id"],
        UUID(current_parent["institution_id"]),
    )
    if not parent:
        raise HTTPException(status_code=404, detail="Parent profile not found.")

    students = get_parent_students(db, parent)
    result = []
    for student in students:
        user = db.query(User).filter(User.id == student.user_id).first()
        class_row = db.execute(
            text("SELECT class_name FROM classes WHERE id = :cid"),
            {"cid": str(student.class_id)},
        ).mappings().first() if student.class_id else None
        present = db.execute(
            text(
                "SELECT COUNT(*) FROM attendance WHERE student_id = :sid "
                "AND institution_id = :iid AND status = 'present'"
            ),
            {"sid": str(student.id), "iid": str(parent.institution_id)},
        ).scalar() or 0
        total = db.execute(
            text(
                "SELECT COUNT(*) FROM attendance WHERE student_id = :sid "
                "AND institution_id = :iid"
            ),
            {"sid": str(student.id), "iid": str(parent.institution_id)},
        ).scalar() or 0
        result.append(
            {
                "id": str(student.id),
                "student_id": student.student_id,
                "full_name": user.full_name if user else None,
                "roll_number": student.roll_number,
                "class_name": class_row["class_name"] if class_row else None,
                "attendance_present": present,
                "attendance_total": total,
                "attendance_percentage": round(present / total * 100, 1) if total else None,
            }
        )
    return result


# ==========================================
# Create Parent
# ==========================================
@router.post(
    "",
    response_model=ParentResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_parent_endpoint(
    parent_data: ParentCreate,
    db: Session = Depends(get_db),
):
    try:
        parent, user = create_parent(
            db,
            parent_data,
        )

        students = get_parent_students(
            db,
            parent,
        )

        student_list = []

        for student in students:
            student_user = (
                db.query(User)
                .filter(User.id == student.user_id)
                .first()
            )

            if student_user:
                student_list.append({
                    "student_id": student.student_id,
                    "full_name": student_user.full_name,
                    "roll_number": student.roll_number,
                    "admission_number": student.admission_number,
                })

        return {
            "id": parent.id,
            "parent_id": parent.parent_id,
            "user_id": parent.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": parent.phone,
            "institution_id": parent.institution_id,
            "students": student_list,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# List Parents
# ==========================================
@router.get(
    "",
    response_model=list[ParentResponse],
)
def list_parents(
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    parents = get_parents(
        db,
        institution_id,
    )

    result = []

    for parent in parents:
        user = get_parent_user(
            db,
            parent,
        )

        if not user:
            continue

        students = get_parent_students(
            db,
            parent,
        )

        student_list = []

        for student in students:
            student_user = (
                db.query(User)
                .filter(User.id == student.user_id)
                .first()
            )

            if student_user:
                student_list.append({
                    "student_id": student.student_id,
                    "full_name": student_user.full_name,
                    "roll_number": student.roll_number,
                    "admission_number": student.admission_number,
                })

        result.append({
            "id": parent.id,
            "parent_id": parent.parent_id,
            "user_id": parent.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": parent.phone,
            "institution_id": parent.institution_id,
            "students": student_list,
        })

    return result


# ==========================================
# Get One Parent
# ==========================================
@router.get(
    "/{parent_id}",
    response_model=ParentResponse,
)
def get_parent_endpoint(
    parent_id: str,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    parent = get_parent(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent not found",
        )

    user = get_parent_user(
        db,
        parent,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent user account not found",
        )

    students = get_parent_students(
        db,
        parent,
    )

    student_list = []

    for student in students:
        student_user = (
            db.query(User)
            .filter(User.id == student.user_id)
            .first()
        )

        if student_user:
            student_list.append({
                "student_id": student.student_id,
                "full_name": student_user.full_name,
                "roll_number": student.roll_number,
                "admission_number": student.admission_number,
            })

    return {
        "id": parent.id,
        "parent_id": parent.parent_id,
        "user_id": parent.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": parent.phone,
        "institution_id": parent.institution_id,
        "students": student_list,
    }


# ==========================================
# Update Parent
# ==========================================
@router.put(
    "/{parent_id}",
    response_model=ParentResponse,
)
def update_parent_endpoint(
    parent_id: str,
    parent_data: ParentUpdate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        parent = update_parent(
            db,
            parent_id,
            institution_id,
            parent_data,
        )

        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent not found",
            )

        user = get_parent_user(
            db,
            parent,
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Parent user account not found",
            )

        students = get_parent_students(
            db,
            parent,
        )

        student_list = []

        for student in students:
            student_user = (
                db.query(User)
                .filter(User.id == student.user_id)
                .first()
            )

            if student_user:
                student_list.append({
                    "student_id": student.student_id,
                    "full_name": student_user.full_name,
                    "roll_number": student.roll_number,
                    "admission_number": student.admission_number,
                })

        return {
            "id": parent.id,
            "parent_id": parent.parent_id,
            "user_id": parent.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": parent.phone,
            "institution_id": parent.institution_id,
            "students": student_list,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# Delete Parent
# ==========================================
@router.delete(
    "/{parent_id}",
)
def delete_parent_endpoint(
    parent_id: str,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_parent(
        db,
        parent_id,
        institution_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent not found",
        )

    return {
        "status": "success",
        "message": "Parent deleted successfully",
    }


# ==========================================
# Add Student to Existing Parent
# ==========================================
@router.post(
    "/{parent_id}/students",
    response_model=ParentStudentResponse,
    status_code=status.HTTP_201_CREATED,
)
def add_student_endpoint(
    parent_id: str,
    student_data: ParentStudentCreate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    student, error = add_student_to_parent(
        db,
        parent_id,
        institution_id,
        student_data,
    )

    if error:
        if error in [
            "Parent not found",
            "Student not found",
        ]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=error,
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    student_user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    if not student_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student user account not found",
        )

    return {
        "student_id": student.student_id,
        "full_name": student_user.full_name,
        "roll_number": student.roll_number,
        "admission_number": student.admission_number,
    }


# ==========================================
# Get Parent's Students
# ==========================================
@router.get(
    "/{parent_id}/students",
    response_model=list[ParentStudentResponse],
)
def get_parent_students_endpoint(
    parent_id: str,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    students = get_students_of_parent(
        db,
        parent_id,
        institution_id,
    )

    if students is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Parent not found",
        )

    result = []

    for student in students:
        student_user = (
            db.query(User)
            .filter(User.id == student.user_id)
            .first()
        )

        if student_user:
            result.append({
                "student_id": student.student_id,
                "full_name": student_user.full_name,
                "roll_number": student.roll_number,
                "admission_number": student.admission_number,
            })

    return result


# ==========================================
# Remove Student from Parent
# ==========================================
@router.delete(
    "/{parent_id}/students/{student_id}",
)
def remove_student_endpoint(
    parent_id: str,
    student_id: str,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    removed, error = remove_student_from_parent(
        db,
        parent_id,
        student_id,
        institution_id,
    )

    if error:
        if error in [
            "Parent not found",
            "Student not found",
        ]:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=error,
            )

        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=error,
        )

    return {
        "status": "success",
        "message": "Student removed from parent successfully",
    }