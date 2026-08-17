import uuid

from sqlalchemy import Column, String, Date, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class LibraryTransaction(Base):
    __tablename__ = "library_transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    student_id = Column(UUID(as_uuid=True), ForeignKey("students.id"), nullable=False)

    book_id = Column(UUID(as_uuid=True), ForeignKey("library_books.id"), nullable=False)

    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"), nullable=True)

    issue_date = Column(Date, nullable=True)

    due_date = Column(Date, nullable=True)

    return_date = Column(Date, nullable=True)

    status = Column(String, nullable=True, default="issued")

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)