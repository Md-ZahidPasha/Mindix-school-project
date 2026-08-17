from uuid import UUID

from sqlalchemy.orm import Session

from app.models.leave_application import LeaveApplication
from app.schemas.leave_application import (
    LeaveApplicationCreate,
    LeaveApplicationUpdate,
)


# ==========================================
# Create Leave Application
# ==========================================
def create_leave_application(
    db: Session,
    leave_data: LeaveApplicationCreate,
):
    data = leave_data.model_dump()
    if data.get("status"):
        data["status"] = data["status"].lower()
    else:
        data["status"] = "pending"

    leave = LeaveApplication(
        **data
    )

    db.add(leave)
    db.commit()
    db.refresh(leave)

    return leave


# ==========================================
# List Leave Applications
# ==========================================
def get_leave_applications(
    db: Session,
    institution_id: UUID,
    employee_id: UUID | None = None,
):
    query = db.query(LeaveApplication).filter(
        LeaveApplication.institution_id == institution_id
    )

    if employee_id:
        query = query.filter(
            LeaveApplication.employee_id == employee_id
        )

    return query.all()


# ==========================================
# Get One Leave Application
# ==========================================
def get_leave_application(
    db: Session,
    leave_id: UUID,
    institution_id: UUID,
):
    return (
        db.query(LeaveApplication)
        .filter(
            LeaveApplication.id == leave_id,
            LeaveApplication.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Update Leave Application
# ==========================================
def update_leave_application(
    db: Session,
    leave_id: UUID,
    institution_id: UUID,
    leave_data: LeaveApplicationUpdate,
):
    leave = get_leave_application(
        db,
        leave_id,
        institution_id,
    )

    if not leave:
        return None

    update_data = leave_data.model_dump(
        exclude_unset=True
    )

    if "status" in update_data and update_data["status"]:
        update_data["status"] = update_data["status"].lower()

    for key, value in update_data.items():
        setattr(leave, key, value)

    db.commit()
    db.refresh(leave)

    return leave


# ==========================================
# Delete Leave Application
# ==========================================
def delete_leave_application(
    db: Session,
    leave_id: UUID,
    institution_id: UUID,
):
    leave = get_leave_application(
        db,
        leave_id,
        institution_id,
    )

    if not leave:
        return None

    db.delete(leave)
    db.commit()

    return leave