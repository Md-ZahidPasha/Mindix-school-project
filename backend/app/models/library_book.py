import uuid

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class LibraryBook(Base):
    __tablename__ = "library_books"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    institution_id = Column(UUID(as_uuid=True), ForeignKey("institutions.id"), nullable=True)

    title = Column(String, nullable=False)

    author = Column(String, nullable=True)

    isbn = Column(String, nullable=True)

    total_copies = Column(Integer, nullable=True, default=1)

    available_copies = Column(Integer, nullable=True, default=1)

    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=True)