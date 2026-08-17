import uuid

from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.connection import Base


class ScheduleEntry(Base):
    """A single persistent timetable slot for an institution.

    Mapped to the additive ``schedule_entries`` table. The table is created by
    running the migration in ``docs/supabase_schedule_entries.sql`` against the
    existing Supabase database. No existing table is altered.
    """

    __tablename__ = "schedule_entries"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
    )

    institution_id = Column(
        UUID(as_uuid=True),
        ForeignKey("institutions.id", ondelete="CASCADE"),
        nullable=False,
    )

    class_id = Column(
        UUID(as_uuid=True),
        ForeignKey("classes.id", ondelete="CASCADE"),
        nullable=False,
    )

    section = Column(
        String,
        nullable=True,
    )

    subject_id = Column(
        UUID(as_uuid=True),
        ForeignKey("subjects.id", ondelete="CASCADE"),
        nullable=True,
    )

    subject_name = Column(
        String,
        nullable=False,
    )

    teacher_id = Column(
        UUID(as_uuid=True),
        ForeignKey("teachers.id", ondelete="SET NULL"),
        nullable=True,
    )

    teacher_name = Column(
        String,
        nullable=True,
    )

    room_id = Column(
        UUID(as_uuid=True),
        ForeignKey("rooms.id", ondelete="SET NULL"),
        nullable=True,
    )

    room_name = Column(
        String,
        nullable=True,
    )

    day = Column(
        String,
        nullable=False,
    )

    period = Column(
        Integer,
        nullable=False,
    )

    source = Column(
        String,
        nullable=False,
        default="manual",
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )