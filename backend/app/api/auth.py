from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.auth import (
    InstitutionLoginRequest,
    InstitutionLoginResponse,
    StudentLoginRequest,
    StudentLoginResponse,
    ParentLoginRequest,
    ParentLoginResponse,
    StaffLoginRequest,
    StaffLoginResponse,
)

from app.services.auth_service import (
    login_institution,
    login_student,
    login_parent,
    login_staff,
)


router = APIRouter(
    prefix="/api/auth",
    tags=["Authentication"],
)


# ==========================================
# Institution Login
# ==========================================
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
            detail="Invalid institution name or password.",
        )

    return result


# ==========================================
# Student Login
# ==========================================
@router.post(
    "/student-login",
    response_model=StudentLoginResponse,
)
def student_login(
    login_data: StudentLoginRequest,
    db: Session = Depends(get_db),
):
    result = login_student(
        db,
        login_data,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid student ID or password.",
        )

    return result


# ==========================================
# Parent Login
# ==========================================
@router.post(
    "/parent-login",
    response_model=ParentLoginResponse,
)
def parent_login(
    login_data: ParentLoginRequest,
    db: Session = Depends(get_db),
):
    result = login_parent(
        db,
        login_data,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid parent ID or password.",
        )

    return result


# ==========================================
# Staff / Employee Login
# ==========================================
@router.post(
    "/staff-login",
    response_model=StaffLoginResponse,
)
def staff_login(
    login_data: StaffLoginRequest,
    db: Session = Depends(get_db),
):
    result = login_staff(
        db,
        login_data,
    )

    if result is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid institution name, email or password.",
        )

    return result