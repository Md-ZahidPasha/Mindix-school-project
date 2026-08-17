from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class SubstituteSuggestionRequest(BaseModel):
    leave_application_id: UUID


class SubstituteSuggestion(BaseModel):
    leave_application_id: UUID
    teacher_id: UUID | None = None
    substitute_teacher_id: UUID
    substitute_name: str
    class_id: UUID
    class_name: str | None = None
    subject_id: UUID | None = None
    subject_name: str | None = None
    day_of_week: str
    period: int
    score: int | None = None
    reason: str | None = None


class SubstitutionCreate(BaseModel):
    leave_application_id: UUID
    teacher_id: UUID | None = None
    substitute_teacher_id: UUID
    class_id: UUID
    subject_id: UUID | None = None
    day_of_week: str
    period: int


class SubstitutionResponse(BaseModel):
    id: UUID
    institution_id: UUID | None = None
    leave_application_id: UUID | None = None
    teacher_id: UUID | None = None
    substitute_teacher_id: UUID | None = None
    class_id: UUID | None = None
    subject_id: UUID | None = None
    day_of_week: str | None = None
    period: int | None = None
    status: str | None = None
    confirmed_by: UUID | None = None
    created_at: datetime | None = None
    teacher_name: str | None = None
    substitute_name: str | None = None
    class_name: str | None = None
    subject_name: str | None = None
    leave_type: str | None = None
    leave_start: str | None = None
    leave_end: str | None = None

    model_config = {"from_attributes": True}