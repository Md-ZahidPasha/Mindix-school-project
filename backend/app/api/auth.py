from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.auth import (
    InstitutionLoginRequest,
    InstitutionLoginResponse,
)
from app.services.auth_service import login_institution

router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=InstitutionLoginResponse,
)
def login(
    login_data: InstitutionLoginRequest,
    db: Session = Depends(get_db),
):
    result = login_institution(
        db,
        login_data,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid institution name or password."
        )

    return result