from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.parent import (
    ParentCreate,
    ParentResponse,
)

from app.services.parent_service import create_parent


router = APIRouter(
    prefix="/api/parents",
    tags=["Parents"],
)


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
        parent, user, student = create_parent(
            db,
            parent_data,
        )

        return {
            "id": parent.id,
            "parent_id": parent.parent_id,
            "user_id": parent.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": parent.phone,
            "student_id": student.student_id,
            "institution_id": parent.institution_id,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )