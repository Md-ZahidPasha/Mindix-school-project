import uuid

from sqlalchemy import Column, String, Date, DateTime, ForeignKey, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class Principal(Base):
    __tablename__ = "principals"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id = Column(
        UUID(as_uuid=True),
        ForeignKey("users.id"),
        nullable=False,
        unique=True
    )

    principal_id = Column(
        String,
        unique=True,
        nullable=False
    )

    qualification = Column(
        String,
        nullable=True
    )

    experience_years = Column(
        Integer,
        nullable=True
    )

    date_of_birth = Column(
        Date,
        nullable=True
    )

    gender = Column(
        String,
        nullable=True
    )

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutions.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False
    )