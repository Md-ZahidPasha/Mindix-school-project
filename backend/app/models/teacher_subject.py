import uuid

from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import UUID

from app.database.connection import Base


class TeacherSubject(Base):
    __tablename__ = "teacher_subjects"

    teacher_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teachers.id"),
        primary_key=True,
        nullable=False,
    )

    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subjects.id"),
        primary_key=True,
        nullable=False,
    )

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=True,
    )