import uuid

from sqlalchemy import (
    Column,
    String,
    Date,
    Time,
    DateTime,
    ForeignKey,
    Numeric,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    student_id = Column(
        UUID(as_uuid=True),
        ForeignKey("students.id"),
        nullable=True,
    )

    class_id = Column(
        UUID(as_uuid=True),
        ForeignKey("classes.id"),
        nullable=True,
    )

    attendance_date = Column(
        Date,
        nullable=False,
    )

    status = Column(
        String,
        nullable=False,
    )

    remarks = Column(
        Text,
        nullable=True,
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=True,
    )

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=True,
    )

    attendance_type = Column(
        String,
        nullable=True,
    )

    teacher_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teachers.id"),
        nullable=True,
    )

    employee_id = Column(
        UUID(as_uuid=True),
        ForeignKey("employees.id"),
        nullable=True,
    )

    period_id = Column(
        UUID(as_uuid=True),
        ForeignKey("periods.id"),
        nullable=True,
    )

    attendance_mode = Column(
        String,
        nullable=True,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=True,
    )

    check_in = Column(
        Time,
        nullable=True,
    )

    check_out = Column(
        Time,
        nullable=True,
    )

    working_hours = Column(
        Numeric,
        nullable=True,
    )