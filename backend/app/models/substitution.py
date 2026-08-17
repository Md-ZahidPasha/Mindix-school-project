import uuid

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class Substitution(Base):
    __tablename__ = "substitutions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"), nullable=True)

    leave_application_id = Column(UUID(as_uuid=True), ForeignKey("leave_applications.id"), nullable=True)

    teacher_id = Column(UUID(as_uuid=True), ForeignKey("teachers.id"), nullable=True)

    substitute_teacher_id = Column(UUID(as_uuid=True), ForeignKey("teachers.id"), nullable=True)

    class_id = Column(UUID(as_uuid=True), ForeignKey("classes.id"), nullable=True)

    subject_id = Column(UUID(as_uuid=True), ForeignKey("subjects.id"), nullable=True)

    day_of_week = Column(String, nullable=True)

    period = Column(Integer, nullable=True)

    status = Column(String, nullable=True, default="suggested")

    confirmed_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)