from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.leave_application import (
    LeaveApplicationCreate,
    LeaveApplicationUpdate,
    LeaveApplicationResponse,
)

from app.services.leave_application_service import (
    create_leave_application,
    get_leave_applications,
    get_leave_application,
    update_leave_application,
    delete_leave_application,
)


router = APIRouter(
    prefix="/api/leave-applications",
    tags=["Leave Applications"],
)


# ==========================================
# Create Leave Application
# ==========================================
@router.post(
    "",
    response_model=LeaveApplicationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_leave_application_endpoint(
    leave_data: LeaveApplicationCreate,
    db: Session = Depends(get_db),
):
    return create_leave_application(
        db,
        leave_data,
    )


# ==========================================
# List Leave Applications
# ==========================================
@router.get(
    "",
    response_model=list[LeaveApplicationResponse],
)
def list_leave_applications(
    institution_id: UUID,
    employee_id: UUID | None = None,
    db: Session = Depends(get_db),
):
    return get_leave_applications(
        db,
        institution_id,
        employee_id,
    )


# ==========================================
# Get One Leave Application
# ==========================================
@router.get(
    "/{leave_id}",
    response_model=LeaveApplicationResponse,
)
def get_leave_application_endpoint(
    leave_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    leave = get_leave_application(
        db,
        leave_id,
        institution_id,
    )

    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leave application not found",
        )

    return leave


# ==========================================
# Update Leave Application
# ==========================================
@router.put(
    "/{leave_id}",
    response_model=LeaveApplicationResponse,
)
def update_leave_application_endpoint(
    leave_id: UUID,
    leave_data: LeaveApplicationUpdate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    leave = update_leave_application(
        db,
        leave_id,
        institution_id,
        leave_data,
    )

    if not leave:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leave application not found",
        )

    return leave


# ==========================================
# Delete Leave Application
# ==========================================
@router.delete(
    "/{leave_id}",
)
def delete_leave_application_endpoint(
    leave_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_leave_application(
        db,
        leave_id,
        institution_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Leave application not found",
        )

    return {
        "status": "success",
        "message": "Leave application deleted successfully",
    }