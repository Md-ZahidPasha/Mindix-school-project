from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import (
    InstitutionCreateRequest,
    InstitutionCreateResponse,
)
from app.services.institution_service import (
    create_institution,
    get_institution_by_email,
    get_institution_by_name,
)

router = APIRouter(
    prefix="/api/institution",
    tags=["Institution"]
)


@router.post(
    "/register",
    response_model=InstitutionCreateResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_institution(
    institution: InstitutionCreateRequest,
    db: Session = Depends(get_db),
):
    # Check duplicate institution name
    existing_institution = get_institution_by_name(
        db,
        institution.institution_name
    )

    if existing_institution:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Institution already exists."
        )

    # Check duplicate email
    existing_email = get_institution_by_email(
        db,
        institution.email
    )

    if existing_email:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Email already registered."
        )

    new_institution = create_institution(
        db,
        institution
    )

    return InstitutionCreateResponse(
        message="Institution registered successfully.",
        institution_id=str(new_institution.id),
        institution_name=new_institution.institution_name,
    )