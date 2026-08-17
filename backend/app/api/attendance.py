from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db

from app.schemas.attendance import (
    AttendanceCreate,
    AttendanceUpdate,
    AttendanceResponse,
)

from app.services.attendance_service import (
    create_attendance,
    get_attendance_records,
    get_attendance,
    update_attendance,
    delete_attendance,
    check_in_employee,
    check_out_employee,
)


router = APIRouter(
    prefix="/api/attendance",
    tags=["Attendance"],
)
security = HTTPBearer()

STAFF_ROLES = {"admin", "principal", "teacher", "staff"}


def _require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if (user.get("role") or "").lower() not in STAFF_ROLES:
        raise HTTPException(status_code=403, detail="Staff authorization is required.")
    if not user.get("institution_id"):
        raise HTTPException(status_code=401, detail="Token is missing the institution scope.")
    return user


# ==========================================
# Create Attendance
# ==========================================
@router.post(
    "",
    response_model=AttendanceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_attendance_endpoint(
    attendance_data: AttendanceCreate,
    db: Session = Depends(get_db),
):
    try:
        return create_attendance(db, attendance_data)
    except ValueError as error:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=str(error)) from error


# ==========================================
# List Attendance
# ==========================================
@router.get(
    "",
    response_model=list[AttendanceResponse],
)
def list_attendance(
    institution_id: UUID | None = None,
    employee_id: UUID | None = None,
    student_id: UUID | None = None,
    db: Session = Depends(get_db),
):
    return get_attendance_records(
        db,
        institution_id=institution_id,
        employee_id=employee_id,
        student_id=student_id,
    )


# ==========================================
# Get One Attendance
# ==========================================
@router.get(
    "/{attendance_id}",
    response_model=AttendanceResponse,
)
def get_attendance_endpoint(
    attendance_id: UUID,
    db: Session = Depends(get_db),
):
    attendance = get_attendance(
        db,
        attendance_id,
    )

    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return attendance


# ==========================================
# Update Attendance
# ==========================================
@router.put(
    "/{attendance_id}",
    response_model=AttendanceResponse,
)
def update_attendance_endpoint(
    attendance_id: UUID,
    attendance_data: AttendanceUpdate,
    db: Session = Depends(get_db),
):
    attendance = update_attendance(
        db,
        attendance_id,
        attendance_data,
    )

    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return attendance


# ==========================================
# Delete Attendance
# ==========================================
@router.delete(
    "/{attendance_id}",
)
def delete_attendance_endpoint(
    attendance_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_attendance(
        db,
        attendance_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Attendance record not found",
        )

    return {
        "status": "success",
        "message": "Attendance record deleted successfully",
    }


# ==========================================
# QR / Student-ID Attendance
# ==========================================
@router.get("/scan/lookup")
def scan_lookup(
    student_id: str,
    institution_id: UUID,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    """Resolve a human-readable student ID (e.g. STU001) or QR code value."""
    row = db.execute(
        text(
            "SELECT s.id AS student_id, s.student_id AS code, s.roll_number, "
            "u.full_name, u.email, c.class_name, c.section "
            "FROM students s "
            "JOIN users u ON u.id = s.user_id "
            "LEFT JOIN classes c ON c.id = s.class_id "
            "WHERE (s.student_id = :code OR s.roll_number = :code) "
            "AND s.institution_id = :iid "
            "ORDER BY s.student_id LIMIT 1"
        ),
        {"code": student_id.strip(), "iid": str(institution_id)},
    ).mappings().first()

    if not row:
        raise HTTPException(status_code=404, detail="No student found for this ID.")

    # Today's attendance status (duplicate detection)
    att = db.execute(
        text(
            "SELECT status FROM attendance WHERE student_id = :sid "
            "AND institution_id = :iid AND attendance_date = CURRENT_DATE "
            "ORDER BY created_at DESC LIMIT 1"
        ),
        {"sid": str(row["student_id"]), "iid": str(institution_id)},
    ).mappings().first()

    return {
        "student_id": str(row["student_id"]),
        "code": row["code"],
        "roll_number": row["roll_number"],
        "full_name": row["full_name"],
        "email": row["email"],
        "class_name": row["class_name"],
        "section": row["section"],
        "attendance_date": str(date.today()),
        "already_marked": bool(att),
        "today_status": att["status"] if att else None,
    }


@router.post("/scan")
def scan_record(
    student_id: UUID,
    class_id: UUID | None = None,
    institution_id: UUID = None,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    """Record attendance from a QR / student-ID scan for the current date."""
    attendance_data = AttendanceCreate(
        student_id=student_id,
        class_id=class_id,
        attendance_date=date.today(),
        status="present",
        institution_id=institution_id,
        attendance_type="student",
        teacher_id=(
            UUID(user["teacher_id"]) if user.get("teacher_id") else None
        ),
        attendance_mode="full_day",
    )
    try:
        created = create_attendance(db, attendance_data)
    except ValueError as error:
        raise HTTPException(status_code=409, detail=str(error))
    except Exception as error:
        print("Scan attendance error:", repr(error))
        raise HTTPException(status_code=500, detail="Failed to record attendance.")

    student = db.execute(
        text(
            "SELECT s.id, s.student_id AS code, u.full_name "
            "FROM students s JOIN users u ON u.id = s.user_id WHERE s.id = :sid"
        ),
        {"sid": str(student_id)},
    ).mappings().first()

    return {
        "status": "success",
        "message": "Attendance recorded successfully.",
        "attendance_id": str(created.id),
        "attendance_date": str(date.today()),
        "student": {
            "id": str(student["id"]) if student else str(student_id),
            "code": student["code"] if student else None,
            "full_name": student["full_name"] if student else None,
        },
    }


# ==========================================
# Employee Check In
# ==========================================
@router.post(
    "/employee/{employee_id}/check-in",
    response_model=AttendanceResponse,
)
def employee_check_in(
    employee_id: UUID,
    institution_id: UUID,
    attendance_date: date | None = None,
    db: Session = Depends(get_db),
):
    if attendance_date is None:
        attendance_date = date.today()

    attendance = check_in_employee(
        db,
        employee_id,
        institution_id,
        attendance_date,
    )

    return attendance


# ==========================================
# Employee Check Out
# ==========================================
@router.post(
    "/employee/{employee_id}/check-out",
    response_model=AttendanceResponse,
)
def employee_check_out(
    employee_id: UUID,
    institution_id: UUID,
    attendance_date: date | None = None,
    db: Session = Depends(get_db),
):
    if attendance_date is None:
        attendance_date = date.today()

    attendance = check_out_employee(
        db,
        employee_id,
        institution_id,
        attendance_date,
    )

    if not attendance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No attendance record or check-in found for this employee",
        )

    return attendance
