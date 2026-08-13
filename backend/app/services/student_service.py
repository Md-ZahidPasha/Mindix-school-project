from uuid import UUID

from sqlalchemy.orm import Session

from app.models.student import Student
from app.models.user import User
from app.schemas.student import StudentCreate, StudentUpdate
from app.core.security import hash_password


def generate_student_id(db: Session) -> str:
    """
    Generate the next human-readable student ID.

    Example:
    STU001
    STU002
    STU003
    """

    students = (
        db.query(Student.student_id)
        .filter(Student.student_id.isnot(None))
        .all()
    )

    max_number = 0

    for (student_id,) in students:
        if not student_id:
            continue

        if student_id.startswith("STU"):
            try:
                number = int(student_id[3:])
                max_number = max(max_number, number)
            except ValueError:
                continue

    return f"STU{max_number + 1:03d}"


def create_student(
    db: Session,
    student_data: StudentCreate
):
    # Check whether email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == student_data.email)
        .first()
    )

    if existing_user:
        raise ValueError(
            "A user with this email already exists"
        )

    # Check whether roll number already exists
    existing_student = (
        db.query(Student)
        .filter(
            Student.roll_number == student_data.roll_number
        )
        .first()
    )

    if existing_student:
        raise ValueError(
            "A student with this roll number already exists"
        )

    # Automatically generate human-readable Student ID
    student_id = generate_student_id(db)

    # Create user account
    user = User(
        institution_id=student_data.institution_id,
        full_name=student_data.full_name,
        email=student_data.email,
        phone=student_data.phone,
        password_hash=hash_password(
            student_data.password
        ),
        role="student",
        status="active",
    )

    db.add(user)
    db.flush()

    # Create student profile
    student = Student(
        student_id=student_id,
        user_id=user.id,
        class_id=student_data.class_id,
        roll_number=student_data.roll_number,
        admission_number=student_data.admission_number,
        date_of_birth=student_data.date_of_birth,
        gender=student_data.gender,
        institution_id=student_data.institution_id,
    )

    db.add(student)
    db.commit()

    db.refresh(student)
    db.refresh(user)

    return student, user


def get_students(
    db: Session,
    institution_id: UUID
):
    return (
        db.query(Student)
        .filter(
            Student.institution_id == institution_id
        )
        .all()
    )


def get_student(
    db: Session,
    student_id: UUID,
    institution_id: UUID
):
    return (
        db.query(Student)
        .filter(
            Student.id == student_id,
            Student.institution_id == institution_id
        )
        .first()
    )


def update_student(
    db: Session,
    student_id: UUID,
    institution_id: UUID,
    student_data: StudentUpdate
):
    student = get_student(
        db,
        student_id,
        institution_id
    )

    if not student:
        return None

    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    data = student_data.model_dump(
        exclude_unset=True
    )

    # Student-specific fields
    student_fields = {
        "roll_number",
        "admission_number",
        "date_of_birth",
        "gender",
        "class_id",
    }

    for field in student_fields:
        if field in data:
            setattr(
                student,
                field,
                data[field]
            )

    # User fields
    if user:
        if "full_name" in data:
            user.full_name = data["full_name"]

        if "email" in data:
            user.email = data["email"]

        if "phone" in data:
            user.phone = data["phone"]

    db.commit()
    db.refresh(student)

    return student


def delete_student(
    db: Session,
    student_id: UUID,
    institution_id: UUID
):
    student = get_student(
        db,
        student_id,
        institution_id
    )

    if not student:
        return None

    user = (
        db.query(User)
        .filter(User.id == student.user_id)
        .first()
    )

    db.delete(student)

    if user:
        db.delete(user)

    db.commit()

    return True