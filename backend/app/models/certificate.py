import uuid

from sqlalchemy import Column, String, Text, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class Certificate(Base):
    __tablename__ = "certificates"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)

    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"), nullable=True)

    requested_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    certificate_name = Column(String, nullable=False)

    certificate_type = Column(String, nullable=True)

    purpose = Column(Text, nullable=True)

    status = Column(String, nullable=True, default="pending")

    certificate_number = Column(String, nullable=True)

    approved_by = Column(UUID(as_uuid=True), ForeignKey("users.id"), nullable=True)

    rejection_reason = Column(Text, nullable=True)

    issue_date = Column(Date, nullable=True)

    reviewed_at = Column(DateTime(timezone=True), nullable=True)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)