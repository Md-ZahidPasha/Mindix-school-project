from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.principal import (
    PrincipalCreate,
    PrincipalResponse,
)
from app.services.principal_service import (
    create_principal,
)


router = APIRouter(
    prefix="/api/principals",
    tags=["Principals"],
)


@router.post(
    "",
    response_model=PrincipalResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_principal_endpoint(
    principal_data: PrincipalCreate,
    db: Session = Depends(get_db),
):
    try:
        principal, user = create_principal(
            db,
            principal_data
        )

        return {
            "id": principal.id,
            "user_id": principal.user_id,

            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,

            "principal_id": principal.principal_id,
            "qualification": principal.qualification,
            "experience_years": principal.experience_years,
            "date_of_birth": principal.date_of_birth,
            "gender": principal.gender,

            "institution_id": principal.institution_id,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )