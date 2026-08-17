from sqlalchemy.orm import Session

from app.models.institution import Institution
from app.models.student import Student
from app.models.parent import Parent
from app.models.user import User
from app.models.employee import Employee
from app.models.teacher import Teacher

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

from app.core.security import (
    verify_password,
    create_access_token,
)

STAFF_ROLES = {"principal", "teacher", "staff", "employee"}


# ==========================================
# Institution Login
# ==========================================
def login_institution(
    db: Session,
    login_data: InstitutionLoginRequest,
):
    institution = (
        db.query(Institution)
        .filter(
            Institution.institution_name
            == login_data.institution_name
        )
        .first()
    )

    if not institution:
        return None

    if not verify_password(
        login_data.password,
        institution.password_hash,
    ):
        return None

    access_token = create_access_token(
        data={
            "institution_id": str(institution.id),
            "institution_name": institution.institution_name,
            "role": "admin",
        }
    )

    return InstitutionLoginResponse(
        message="Login successful",
        institution_id=str(institution.id),
        institution_name=institution.institution_name,
        user_id=str(institution.id),
        role="admin",
        access_token=access_token,
        token_type="bearer",
    )


# ==========================================
# Student Login
# ==========================================
def login_student(
    db: Session,
    login_data: StudentLoginRequest,
):
    student = (
        db.query(Student)
        .filter(
            Student.student_id == login_data.student_id
        )
        .first()
    )

    if not student:
        return None

    user = (
        db.query(User)
        .filter(
            User.id == student.user_id
        )
        .first()
    )

    if not user:
        return None

    if user.role != "student":
        return None

    if user.status != "active":
        return None

    if not verify_password(
        login_data.password,
        user.password_hash,
    ):
        return None

    access_token = create_access_token(
        data={
            "user_id": str(user.id),
            "student_id": student.student_id,
            "institution_id": str(student.institution_id),
            "role": "student",
        }
    )

    return StudentLoginResponse(
        message="Login successful",
        student_id=student.student_id,
        user_id=str(user.id),
        institution_id=str(student.institution_id),
        role="student",
        full_name=user.full_name,
        access_token=access_token,
        token_type="bearer",
    )


# ==========================================
# Parent Login
# ==========================================
def login_parent(
    db: Session,
    login_data: ParentLoginRequest,
):
    # Find parent using human-readable Parent ID
    parent = (
        db.query(Parent)
        .filter(
            Parent.parent_id == login_data.parent_id
        )
        .first()
    )

    if not parent:
        return None

    # Find the corresponding user account
    user = (
        db.query(User)
        .filter(
            User.id == parent.user_id
        )
        .first()
    )

    if not user:
        return None

    # Make sure the account is actually a parent
    if user.role != "parent":
        return None

    # Make sure the account is active
    if user.status != "active":
        return None

    # Verify password stored in users.password_hash
    if not verify_password(
        login_data.password,
        user.password_hash,
    ):
        return None

    # Create parent JWT
    access_token = create_access_token(
        data={
            "user_id": str(user.id),
            "parent_id": parent.parent_id,
            "institution_id": str(parent.institution_id),
            "role": "parent",
        }
    )

    return ParentLoginResponse(
        message="Login successful",
        parent_id=parent.parent_id,
        user_id=str(user.id),
        institution_id=str(parent.institution_id),
        role="parent",
        full_name=user.full_name,
        access_token=access_token,
        token_type="bearer",
    )


# ==========================================
# Staff / Employee Login
# ==========================================
def login_staff(
    db: Session,
    login_data: StaffLoginRequest,
):
    institution = (
        db.query(Institution)
        .filter(
            Institution.institution_name == login_data.institution_name
        )
        .first()
    )

    if not institution:
        return None

    user = (
        db.query(User)
        .filter(
            User.email == login_data.email,
            User.institution_id == institution.id,
        )
        .first()
    )

    if not user:
        return None

    role = (user.role or "").lower()
    if role not in STAFF_ROLES:
        return None

    if user.status != "active":
        return None

    if not verify_password(login_data.password, user.password_hash):
        return None

    employee_id = None
    teacher_id = None
    if role == "employee":
        employee = (
            db.query(Employee)
            .filter(
                Employee.user_id == user.id,
                Employee.institution_id == institution.id,
            )
            .first()
        )
        employee_id = str(employee.id) if employee else None
    elif role == "teacher":
        teacher = (
            db.query(Teacher)
            .filter(
                Teacher.user_id == user.id,
                Teacher.institution_id == institution.id,
            )
            .first()
        )
        teacher_id = str(teacher.id) if teacher else None

    access_token = create_access_token(
        data={
            "user_id": str(user.id),
            "institution_id": str(institution.id),
            "role": role,
            "teacher_id": teacher_id,
            "employee_id": employee_id,
        }
    )

    return StaffLoginResponse(
        message="Login successful",
        user_id=str(user.id),
        institution_id=str(institution.id),
        role=role,
        full_name=user.full_name,
        access_token=access_token,
        token_type="bearer",
        employee_id=employee_id,
        teacher_id=teacher_id,
    )