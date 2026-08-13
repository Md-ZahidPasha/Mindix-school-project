from uuid import UUID

from sqlalchemy.orm import Session

from app.models.parent import Parent
from app.models.student_parent import StudentParent
from app.models.student import Student
from app.models.user import User

from app.schemas.parent import ParentCreate

from app.core.security import hash_password


def generate_parent_id(db: Session) -> str:
    parents = (
        db.query(Parent.parent_id)
        .filter(Parent.parent_id.isnot(None))
        .all()
    )

    max_number = 0

    for (parent_id,) in parents:
        if parent_id and parent_id.startswith("PAR"):
            try:
                number = int(parent_id[3:])
                max_number = max(max_number, number)
            except ValueError:
                continue

    return f"PAR{max_number + 1:03d}"


def create_parent(
    db: Session,
    parent_data: ParentCreate,
):
    # Check email
    existing_user = (
        db.query(User)
        .filter(User.email == parent_data.email)
        .first()
    )

    if existing_user:
        raise ValueError(
            "A user with this email already exists"
        )

    # Find student using human-readable Student ID
    student = (
        db.query(Student)
        .filter(
            Student.student_id == parent_data.student_id,
            Student.institution_id == parent_data.institution_id,
        )
        .first()
    )

    if not student:
        raise ValueError(
            "Student not found for the given Student ID"
        )

    # Generate Parent ID
    parent_id = generate_parent_id(db)

    # Create user account
    user = User(
        institution_id=parent_data.institution_id,
        full_name=parent_data.full_name,
        email=parent_data.email,
        phone=parent_data.phone,
        password_hash=hash_password(parent_data.password),
        role="parent",
        status="active",
    )

    db.add(user)
    db.flush()

    # Create parent profile
    parent = Parent(
        user_id=user.id,
        parent_id=parent_id,
        phone=parent_data.phone,
        institution_id=parent_data.institution_id,
    )

    db.add(parent)
    db.flush()

    # Link parent to student
    student_parent = StudentParent(
        student_id=student.id,
        parent_id=parent.id,
        institution_id=parent_data.institution_id,
    )

    db.add(student_parent)

    db.commit()

    db.refresh(parent)
    db.refresh(user)

    return parent, user, student