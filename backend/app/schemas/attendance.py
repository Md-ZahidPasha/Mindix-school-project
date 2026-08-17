from datetime import date, time, datetime
from decimal import Decimal
from uuid import UUID

from pydantic import BaseModel


# ==========================================
# Create Attendance
# ==========================================
class AttendanceCreate(BaseModel):
    student_id: UUID | None = None
    class_id: UUID | None = None

    attendance_date: date
    status: str

    remarks: str | None = None
    institution_id: UUID | None = None

    attendance_type: str | None = None
    teacher_id: UUID | None = None
    employee_id: UUID | None = None
    period_id: UUID | None = None

    attendance_mode: str | None = None

    check_in: time | None = None
    check_out: time | None = None
    working_hours: Decimal | None = None


# ==========================================
# Update Attendance
# ==========================================
class AttendanceUpdate(BaseModel):
    student_id: UUID | None = None
    class_id: UUID | None = None

    attendance_date: date | None = None
    status: str | None = None

    remarks: str | None = None
    institution_id: UUID | None = None

    attendance_type: str | None = None
    teacher_id: UUID | None = None
    employee_id: UUID | None = None
    period_id: UUID | None = None

    attendance_mode: str | None = None

    check_in: time | None = None
    check_out: time | None = None
    working_hours: Decimal | None = None


# ==========================================
# Attendance Response
# ==========================================
class AttendanceResponse(BaseModel):
    id: UUID

    student_id: UUID | None = None
    class_id: UUID | None = None

    attendance_date: date
    status: str

    remarks: str | None = None
    created_at: datetime | None = None
    institution_id: UUID | None = None

    attendance_type: str | None = None
    teacher_id: UUID | None = None
    employee_id: UUID | None = None
    period_id: UUID | None = None

    attendance_mode: str | None = None
    updated_at: datetime | None = None

    check_in: time | None = None
    check_out: time | None = None
    working_hours: Decimal | None = None

    class Config:
        from_attributes = True