from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.employee import (
    EmployeeCreate,
    EmployeeUpdate,
    EmployeeResponse,
)
from app.services.employee_service import (
    create_employee,
    get_employees,
    get_employee,
    update_employee,
    delete_employee,
    get_employee_user,
)


router = APIRouter(
    prefix="/api/employees",
    tags=["Employees"],
)


# ==========================================
# Create Employee
# ==========================================
@router.post(
    "",
    response_model=EmployeeResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_employee_endpoint(
    employee_data: EmployeeCreate,
    db: Session = Depends(get_db),
):
    try:
        employee, user = create_employee(
            db,
            employee_data,
        )

        return {
            "id": employee.id,
            "user_id": employee.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "designation": employee.designation,
            "department_id": employee.department_id,
            "joining_date": employee.joining_date,
            "institution_id": employee.institution_id,
            "employee_code": employee.employee_code,
            "alternate_phone": employee.alternate_phone,
            "employment_type": employee.employment_type,
            "address": employee.address,
            "city": employee.city,
            "state": employee.state,
            "pincode": employee.pincode,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# List Employees
# ==========================================
@router.get(
    "",
    response_model=list[EmployeeResponse],
)
def list_employees(
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    employees = get_employees(
        db,
        institution_id,
    )

    result = []

    for employee in employees:
        user = get_employee_user(
            db,
            employee,
        )

        if not user:
            continue

        result.append({
            "id": employee.id,
            "user_id": employee.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "designation": employee.designation,
            "department_id": employee.department_id,
            "joining_date": employee.joining_date,
            "institution_id": employee.institution_id,
            "employee_code": employee.employee_code,
            "alternate_phone": employee.alternate_phone,
            "employment_type": employee.employment_type,
            "address": employee.address,
            "city": employee.city,
            "state": employee.state,
            "pincode": employee.pincode,
        })

    return result


# ==========================================
# Employee Dashboard
# ==========================================
@router.get(
    "/{employee_id}/dashboard",
)
def employee_dashboard(
    employee_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    employee = get_employee(
        db,
        employee_id,
        institution_id,
    )

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    user = get_employee_user(
        db,
        employee,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee user account not found",
        )

    # ------------------------------------------
    # Today's attendance
    # Uses only the attendance fields already
    # confirmed in the database.
    # ------------------------------------------
    attendance = db.execute(
        text("""
            SELECT
                check_in,
                check_out,
                working_hours
            FROM attendance
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
            ORDER BY created_at DESC
            LIMIT 1
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).mappings().first()

    # ------------------------------------------
    # Task counts
    # ------------------------------------------
    pending_tasks = db.execute(
        text("""
            SELECT COUNT(*)
            FROM tasks
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
              AND LOWER(COALESCE(status, '')) NOT IN
                  ('completed', 'complete', 'done')
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    completed_tasks = db.execute(
        text("""
            SELECT COUNT(*)
            FROM tasks
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
              AND LOWER(COALESCE(status, '')) IN
                  ('completed', 'complete', 'done')
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    # ------------------------------------------
    # Today's / current schedule
    # ------------------------------------------
    schedules = db.execute(
        text("""
            SELECT
                schedule_date,
                title,
                location,
                route,
                passengers,
                type,
                start_time,
                end_time,
                working_hours
            FROM employee_schedules
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
              AND schedule_date = CURRENT_DATE
            ORDER BY start_time
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).mappings().all()

    # ------------------------------------------
    # Leave applications
    # ------------------------------------------
    pending_leaves = db.execute(
        text("""
            SELECT COUNT(*)
            FROM leave_applications
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
              AND LOWER(COALESCE(status, '')) = 'pending'
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    approved_leaves = db.execute(
        text("""
            SELECT COUNT(*)
            FROM leave_applications
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
              AND LOWER(COALESCE(status, '')) = 'approved'
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    # ------------------------------------------
    # Employee notifications
    # ------------------------------------------
    notification_count = db.execute(
        text("""
            SELECT COUNT(*)
            FROM employee_notifications
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    # ------------------------------------------
    # Employee documents
    # ------------------------------------------
    document_count = db.execute(
        text("""
            SELECT COUNT(*)
            FROM documents
            WHERE employee_id = :employee_id
              AND institution_id = :institution_id
        """),
        {
            "employee_id": employee_id,
            "institution_id": institution_id,
        },
    ).scalar() or 0

    return {
        "employee": {
            "id": str(employee.id),
            "user_id": str(employee.user_id),
            "employee_code": employee.employee_code,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "designation": employee.designation,
            "department_id": (
                str(employee.department_id)
                if employee.department_id
                else None
            ),
        },

        "attendance": (
            dict(attendance)
            if attendance
            else {
                "check_in": None,
                "check_out": None,
                "working_hours": 0,
            }
        ),

        "tasks": {
            "pending": pending_tasks,
            "completed": completed_tasks,
        },

        "schedule": [
            dict(row)
            for row in schedules
        ],

        "leave": {
            "pending_applications": pending_leaves,
            "approved_applications": approved_leaves,
            "balance": None,
        },

        "notifications": {
            "count": notification_count,
        },

        "documents": {
            "count": document_count,
        },
    }


# ==========================================
# Get One Employee
# ==========================================
@router.get(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def get_employee_endpoint(
    employee_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    employee = get_employee(
        db,
        employee_id,
        institution_id,
    )

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    user = get_employee_user(
        db,
        employee,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee user account not found",
        )

    return {
        "id": employee.id,
        "user_id": employee.user_id,
        "full_name": user.full_name,
        "email": user.email,
        "phone": user.phone,
        "designation": employee.designation,
        "department_id": employee.department_id,
        "joining_date": employee.joining_date,
        "institution_id": employee.institution_id,
        "employee_code": employee.employee_code,
        "alternate_phone": employee.alternate_phone,
        "employment_type": employee.employment_type,
        "address": employee.address,
        "city": employee.city,
        "state": employee.state,
        "pincode": employee.pincode,
    }


# ==========================================
# Update Employee
# ==========================================
@router.put(
    "/{employee_id}",
    response_model=EmployeeResponse,
)
def update_employee_endpoint(
    employee_id: UUID,
    employee_data: EmployeeUpdate,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    try:
        employee = update_employee(
            db,
            employee_id,
            institution_id,
            employee_data,
        )

        if not employee:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found",
            )

        user = get_employee_user(
            db,
            employee,
        )

        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee user account not found",
            )

        return {
            "id": employee.id,
            "user_id": employee.user_id,
            "full_name": user.full_name,
            "email": user.email,
            "phone": user.phone,
            "designation": employee.designation,
            "department_id": employee.department_id,
            "joining_date": employee.joining_date,
            "institution_id": employee.institution_id,
            "employee_code": employee.employee_code,
            "alternate_phone": employee.alternate_phone,
            "employment_type": employee.employment_type,
            "address": employee.address,
            "city": employee.city,
            "state": employee.state,
            "pincode": employee.pincode,
        }

    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


# ==========================================
# Delete Employee
# ==========================================
@router.delete(
    "/{employee_id}",
)
def delete_employee_endpoint(
    employee_id: UUID,
    institution_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = delete_employee(
        db,
        employee_id,
        institution_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Employee not found",
        )

    return {
        "status": "success",
        "message": "Employee deleted successfully",
    }