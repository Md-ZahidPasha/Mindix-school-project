from pydantic import BaseModel, Field


class TimetableLesson(BaseModel):
    teacher_id: str
    teacher_name: str
    class_id: str
    class_name: str
    subject: str
    room: str
    sessions_per_week: int = Field(default=1, ge=1, le=10)


class TimetableGenerateRequest(BaseModel):
    lessons: list[TimetableLesson] = Field(min_length=1)
    working_days: list[str] = Field(default=["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    periods_per_day: int = Field(default=6, ge=1, le=12)


class TimetableSlotResponse(BaseModel):
    day: str
    period: int
    teacher_id: str
    teacher_name: str
    class_id: str
    class_name: str
    subject: str
    room: str
