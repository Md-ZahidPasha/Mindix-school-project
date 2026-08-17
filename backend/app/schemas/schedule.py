from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, Field


# ==========================================
# Schedule Entry
# ==========================================
class ScheduleEntryCreate(BaseModel):
    class_id: UUID
    section: str | None = None
    subject_id: UUID | None = None
    subject_name: str
    teacher_id: UUID | None = None
    teacher_name: str | None = None
    room_id: UUID | None = None
    room_name: str | None = None
    day: str
    period: int = Field(ge=1, le=20)


class ScheduleEntryUpdate(BaseModel):
    class_id: UUID | None = None
    section: str | None = None
    subject_id: UUID | None = None
    subject_name: str | None = None
    teacher_id: UUID | None = None
    teacher_name: str | None = None
    room_id: UUID | None = None
    room_name: str | None = None
    day: str | None = None
    period: int | None = Field(default=None, ge=1, le=20)


class ScheduleEntryResponse(BaseModel):
    id: UUID | None = None
    institution_id: UUID
    class_id: UUID
    class_name: str | None = None
    section: str | None = None
    subject_id: UUID | None = None
    subject_name: str
    teacher_id: UUID | None = None
    teacher_name: str | None = None
    room_id: UUID | None = None
    room_name: str | None = None
    day: str
    period: int
    source: str = "manual"
    created_at: datetime | None = None
    updated_at: datetime | None = None


# ==========================================
# Timetable Generation
# ==========================================
class ScheduleGenerateRequest(BaseModel):
    class_ids: list[UUID] | None = Field(
        default=None,
        description="Classes to schedule. Omit to schedule every class in the institution.",
    )
    working_days: list[str] = Field(
        default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    )
    periods_per_day: int = Field(default=6, ge=1, le=12)
    sessions_per_week: int = Field(default=1, ge=1, le=10)
    persist: bool = Field(
        default=True,
        description="Persist generated slots to schedule_entries (replaces previously generated slots).",
    )


class ScheduleGenerateResponse(BaseModel):
    status: str
    message: str
    generated: list[ScheduleEntryResponse]
    skipped: list[dict]
    conflicts: int = 0


# ==========================================
# Conflict Detection
# ==========================================
class ScheduleConflict(BaseModel):
    type: str
    day: str
    period: int
    value: str
    entries: list[UUID]


class ScheduleConflictResponse(BaseModel):
    institution_id: UUID
    conflicts: list[ScheduleConflict]


# ==========================================
# Lookup data for the frontend
# ==========================================
class ScheduleClass(BaseModel):
    id: UUID
    name: str
    section: str | None = None


class ScheduleTeacher(BaseModel):
    id: UUID
    name: str | None = None


class ScheduleSubject(BaseModel):
    id: UUID
    name: str | None = None