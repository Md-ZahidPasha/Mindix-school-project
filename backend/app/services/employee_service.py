from uuid import UUID

from sqlalchemy.orm import Session

from app.models.employee import Employee
from app.models.user import User
from app.schemas.employee import EmployeeCreate, EmployeeUpdate
from app.core.security import hash_password


# ==========================================
# Generate Employee Code
# ==========================================
def generate_employee_code(db: Session) -> str:
    employees = (
        db.query(Employee.employee_code)
        .filter(Employee.employee_code.isnot(None))
        .all()
    )

    max_number = 0

    for (employee_code,) in employees:
        if employee_code and employee_code.startswith("EMP"):
            try:
                number = int(employee_code[3:])
                max_number = max(max_number, number)
            except ValueError:
                continue

    return f"EMP{max_number + 1:03d}"


# ==========================================
# Get Employee User
# ==========================================
def get_employee_user(
    db: Session,
    employee: Employee,
):
    return (
        db.query(User)
        .filter(User.id == employee.user_id)
        .first()
    )


# ==========================================
# Get Employee by ID
# ==========================================
def get_employee(
    db: Session,
    employee_id: UUID,
    institution_id: UUID,
):
    return (
        db.query(Employee)
        .filter(
            Employee.id == employee_id,
            Employee.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Create Employee
# ==========================================
def create_employee(
    db: Session,
    employee_data: EmployeeCreate,
):
    existing_user = (
        db.query(User)
        .filter(User.email == employee_data.email)
        .first()
    )

    if existing_user:
        raise ValueError(
            "A user with this email already exists"
        )

    employee_code = employee_data.employee_code

    if employee_code:
        existing_code = (
            db.query(Employee)
            .filter(Employee.employee_code == employee_code)
            .first()
        )

        if existing_code:
            raise ValueError(
                "An employee with this employee code already exists"
            )
    else:
        employee_code = generate_employee_code(db)

    user = User(
        institution_id=employee_data.institution_id,
        full_name=employee_data.full_name,
        email=employee_data.email,
        phone=employee_data.phone,
        password_hash=hash_password(employee_data.password),
        role="employee",
        status="active",
    )

    db.add(user)
    db.flush()

    employee = Employee(
        user_id=user.id,
        designation=employee_data.designation,
        department_id=employee_data.department_id,
        joining_date=employee_data.joining_date,
        institution_id=employee_data.institution_id,
        employee_code=employee_code,
        alternate_phone=employee_data.alternate_phone,
        employment_type=employee_data.employment_type,
        address=employee_data.address,
        city=employee_data.city,
        state=employee_data.state,
        pincode=employee_data.pincode,
    )

    db.add(employee)
    db.commit()

    db.refresh(employee)
    db.refresh(user)

    return employee, user


# ==========================================
# List Employees
# ==========================================
def get_employees(
    db: Session,
    institution_id: UUID,
):
    return (
        db.query(Employee)
        .filter(
            Employee.institution_id == institution_id
        )
        .all()
    )


# ==========================================
# Update Employee
# ==========================================
def update_employee(
    db: Session,
    employee_id: UUID,
    institution_id: UUID,
    employee_data: EmployeeUpdate,
):
    employee = get_employee(
        db,
        employee_id,
        institution_id,
    )

    if not employee:
        return None

    user = get_employee_user(
        db,
        employee,
    )

    data = employee_data.model_dump(
        exclude_unset=True
    )

    if "email" in data and user:
        existing_user = (
            db.query(User)
            .filter(
                User.email == data["email"],
                User.id != user.id,
            )
            .first()
        )

        if existing_user:
            raise ValueError(
                "A user with this email already exists"
            )

    if "employee_code" in data:
        existing_code = (
            db.query(Employee)
            .filter(
                Employee.employee_code == data["employee_code"],
                Employee.id != employee.id,
            )
            .first()
        )

        if existing_code:
            raise ValueError(
                "An employee with this employee code already exists"
            )

    # User fields
    if user:
        if "full_name" in data:
            user.full_name = data["full_name"]

        if "email" in data:
            user.email = data["email"]

        if "phone" in data:
            user.phone = data["phone"]

    # Employee fields
    employee_fields = [
        "designation",
        "department_id",
        "joining_date",
        "institution_id",
        "employee_code",
        "alternate_phone",
        "employment_type",
        "address",
        "city",
        "state",
        "pincode",
    ]

    for field in employee_fields:
        if field in data:
            setattr(employee, field, data[field])

    db.commit()
    db.refresh(employee)

    return employee


# ==========================================
# Delete Employee
# ==========================================
def delete_employee(
    db: Session,
    employee_id: UUID,
    institution_id: UUID,
):
    employee = get_employee(
        db,
        employee_id,
        institution_id,
    )

    if not employee:
        return None

    user = get_employee_user(
        db,
        employee,
    )

    db.delete(employee)

    if user:
        db.delete(user)

    db.commit()

    return True