from datetime import datetime, time
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.attendance import Attendance
from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
)


# ==========================================
# Create Attendance
# ==========================================
def create_attendance(
    db: Session,
    attendance_data: AttendanceCreate,
):
    # A student may be marked only once per class/session/day. This protects
    # both manual and computer-vision attendance submissions.
    if attendance_data.student_id:
        existing = db.query(Attendance).filter(
            Attendance.student_id == attendance_data.student_id,
            Attendance.attendance_date == attendance_data.attendance_date,
            Attendance.class_id == attendance_data.class_id,
            Attendance.period_id == attendance_data.period_id,
        ).first()
        if existing:
            raise ValueError("Already marked present for this attendance session.")
    attendance = Attendance(
        **attendance_data.model_dump()
    )

    db.add(attendance)
    db.commit()
    db.refresh(attendance)

    return attendance


# ==========================================
# Get Attendance Records
# ==========================================
def get_attendance_records(
    db: Session,
    institution_id: UUID | None = None,
    employee_id: UUID | None = None,
    student_id: UUID | None = None,
):
    query = db.query(Attendance)

    if institution_id:
        query = query.filter(
            Attendance.institution_id == institution_id
        )

    if employee_id:
        query = query.filter(
            Attendance.employee_id == employee_id
        )

    if student_id:
        query = query.filter(
            Attendance.student_id == student_id
        )

    return (
        query
        .order_by(Attendance.attendance_date.desc())
        .all()
    )


# ==========================================
# Get One Attendance
# ==========================================
def get_attendance(
    db: Session,
    attendance_id: UUID,
):
    return (
        db.query(Attendance)
        .filter(
            Attendance.id == attendance_id
        )
        .first()
    )


# ==========================================
# Update Attendance
# ==========================================
def update_attendance(
    db: Session,
    attendance_id: UUID,
    attendance_data: AttendanceUpdate,
):
    attendance = get_attendance(
        db,
        attendance_id,
    )

    if not attendance:
        return None

    data = attendance_data.model_dump(
        exclude_unset=True
    )

    for field, value in data.items():
        setattr(
            attendance,
            field,
            value,
        )

    # Recalculate working hours if both times exist
    if attendance.check_in and attendance.check_out:
        start = datetime.combine(
            attendance.attendance_date,
            attendance.check_in,
        )

        end = datetime.combine(
            attendance.attendance_date,
            attendance.check_out,
        )

        if end >= start:
            duration = end - start
            attendance.working_hours = (
                duration.total_seconds() / 3600
            )

    db.commit()
    db.refresh(attendance)

    return attendance


# ==========================================
# Delete Attendance
# ==========================================
def delete_attendance(
    db: Session,
    attendance_id: UUID,
):
    attendance = get_attendance(
        db,
        attendance_id,
    )

    if not attendance:
        return False

    db.delete(attendance)
    db.commit()

    return True


# ==========================================
# Employee Check In
# ==========================================
def check_in_employee(
    db: Session,
    employee_id: UUID,
    institution_id: UUID,
    attendance_date,
):
    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.employee_id == employee_id,
            Attendance.institution_id == institution_id,
            Attendance.attendance_date == attendance_date,
        )
        .first()
    )

    if not attendance:
        attendance = Attendance(
            employee_id=employee_id,
            institution_id=institution_id,
            attendance_date=attendance_date,
            status="present",
            attendance_type="employee",
            attendance_mode="full_day",
            check_in=datetime.now().time(),
        )

        db.add(attendance)

    else:
        if attendance.check_in:
            return attendance

        attendance.check_in = datetime.now().time()
        attendance.status = "present"

    db.commit()
    db.refresh(attendance)

    return attendance


# ==========================================
# Employee Check Out
# ==========================================
def check_out_employee(
    db: Session,
    employee_id: UUID,
    institution_id: UUID,
    attendance_date,
):
    attendance = (
        db.query(Attendance)
        .filter(
            Attendance.employee_id == employee_id,
            Attendance.institution_id == institution_id,
            Attendance.attendance_date == attendance_date,
        )
        .first()
    )

    if not attendance:
        return None

    if not attendance.check_in:
        return None

    attendance.check_out = datetime.now().time()

    start = datetime.combine(
        attendance.attendance_date,
        attendance.check_in,
    )

    end = datetime.combine(
        attendance.attendance_date,
        attendance.check_out,
    )

    if end >= start:
        duration = end - start
        attendance.working_hours = (
            duration.total_seconds() / 3600
        )

    db.commit()
    db.refresh(attendance)

    return attendance
