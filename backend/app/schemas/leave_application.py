from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel


class LeaveApplicationCreate(BaseModel):
    user_id: UUID
    leave_type: str
    start_date: date
    end_date: date
    reason: str | None = None
    status: str | None = "Pending"
    institution_id: UUID | None = None
    employee_id: UUID | None = None


class LeaveApplicationUpdate(BaseModel):
    leave_type: str | None = None
    start_date: date | None = None
    end_date: date | None = None
    reason: str | None = None
    status: str | None = None
    institution_id: UUID | None = None
    employee_id: UUID | None = None


class LeaveApplicationResponse(BaseModel):
    id: UUID
    user_id: UUID
    leave_type: str
    start_date: date
    end_date: date
    reason: str | None = None
    status: str | None = None
    created_at: datetime | None = None
    institution_id: UUID | None = None
    employee_id: UUID | None = None

    class Config:
        from_attributes = True