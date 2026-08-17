from uuid import UUID

from sqlalchemy.orm import Session

from app.models.parent import Parent
from app.models.student_parent import StudentParent
from app.models.student import Student
from app.models.user import User

from app.schemas.parent import (
    ParentCreate,
    ParentUpdate,
    ParentStudentCreate,
)

from app.core.security import hash_password


# ==========================================
# Generate Parent ID
# ==========================================
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


# ==========================================
# Get Parent by Parent ID
# ==========================================
def get_parent_by_parent_id(
    db: Session,
    parent_id: str,
    institution_id: UUID,
):
    return (
        db.query(Parent)
        .filter(
            Parent.parent_id == parent_id,
            Parent.institution_id == institution_id,
        )
        .first()
    )


# ==========================================
# Get Parent User
# ==========================================
def get_parent_user(
    db: Session,
    parent: Parent,
):
    return (
        db.query(User)
        .filter(User.id == parent.user_id)
        .first()
    )


# ==========================================
# Get Students Linked to Parent
# ==========================================
def get_parent_students(
    db: Session,
    parent: Parent,
):
    return (
        db.query(Student)
        .join(
            StudentParent,
            StudentParent.student_id == Student.id,
        )
        .filter(
            StudentParent.parent_id == parent.id,
            StudentParent.institution_id == parent.institution_id,
        )
        .all()
    )


# ==========================================
# Create Parent
# ==========================================
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

    # Find student
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

    # Link first student
    student_parent = StudentParent(
        student_id=student.id,
        parent_id=parent.id,
        institution_id=parent_data.institution_id,
    )

    db.add(student_parent)

    db.commit()

    db.refresh(parent)
    db.refresh(user)

    return parent, user


# ==========================================
# List Parents
# ==========================================
def get_parents(
    db: Session,
    institution_id: UUID,
):
    return (
        db.query(Parent)
        .filter(
            Parent.institution_id == institution_id
        )
        .all()
    )


# ==========================================
# Get One Parent
# ==========================================
def get_parent(
    db: Session,
    parent_id: str,
    institution_id: UUID,
):
    return get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )


# ==========================================
# Update Parent
# ==========================================
def update_parent(
    db: Session,
    parent_id: str,
    institution_id: UUID,
    parent_data: ParentUpdate,
):
    parent = get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        return None

    user = get_parent_user(
        db,
        parent,
    )

    data = parent_data.model_dump(
        exclude_unset=True
    )

    # Check email if changing
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

    # Update parent/user information
    if user:
        if "full_name" in data:
            user.full_name = data["full_name"]

        if "email" in data:
            user.email = data["email"]

        if "phone" in data:
            user.phone = data["phone"]

    if "phone" in data:
        parent.phone = data["phone"]

    db.commit()

    db.refresh(parent)

    return parent


# ==========================================
# Delete Parent
# ==========================================
def delete_parent(
    db: Session,
    parent_id: str,
    institution_id: UUID,
):
    parent = get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        return None

    user = get_parent_user(
        db,
        parent,
    )

    # Delete parent-student relationships
    db.query(StudentParent).filter(
        StudentParent.parent_id == parent.id,
        StudentParent.institution_id == institution_id,
    ).delete(
        synchronize_session=False
    )

    # Delete parent
    db.delete(parent)

    # Delete user account
    if user:
        db.delete(user)

    db.commit()

    return True


# ==========================================
# Add Student to Existing Parent
# ==========================================
def add_student_to_parent(
    db: Session,
    parent_id: str,
    institution_id: UUID,
    student_data: ParentStudentCreate,
):
    parent = get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        return None, "Parent not found"

    # Find student
    student = (
        db.query(Student)
        .filter(
            Student.student_id == student_data.student_id,
            Student.institution_id == institution_id,
        )
        .first()
    )

    if not student:
        return None, "Student not found"

    # Check if already linked
    existing_link = (
        db.query(StudentParent)
        .filter(
            StudentParent.student_id == student.id,
            StudentParent.parent_id == parent.id,
            StudentParent.institution_id == institution_id,
        )
        .first()
    )

    if existing_link:
        return None, "Student is already linked to this parent"

    # Create relationship
    student_parent = StudentParent(
        student_id=student.id,
        parent_id=parent.id,
        institution_id=institution_id,
    )

    db.add(student_parent)
    db.commit()

    db.refresh(student_parent)

    return student, None


# ==========================================
# Get All Students of Parent
# ==========================================
def get_students_of_parent(
    db: Session,
    parent_id: str,
    institution_id: UUID,
):
    parent = get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        return None

    return get_parent_students(
        db,
        parent,
    )


# ==========================================
# Remove Student from Parent
# ==========================================
def remove_student_from_parent(
    db: Session,
    parent_id: str,
    student_id: str,
    institution_id: UUID,
):
    parent = get_parent_by_parent_id(
        db,
        parent_id,
        institution_id,
    )

    if not parent:
        return None, "Parent not found"

    student = (
        db.query(Student)
        .filter(
            Student.student_id == student_id,
            Student.institution_id == institution_id,
        )
        .first()
    )

    if not student:
        return None, "Student not found"

    relationship = (
        db.query(StudentParent)
        .filter(
            StudentParent.parent_id == parent.id,
            StudentParent.student_id == student.id,
            StudentParent.institution_id == institution_id,
        )
        .first()
    )

    if not relationship:
        return None, "Student is not linked to this parent"

    db.delete(relationship)
    db.commit()

    return True, None