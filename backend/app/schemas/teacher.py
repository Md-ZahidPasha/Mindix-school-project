from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, EmailStr


class TeacherCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str

    institution_id: UUID | None = None
    department_id: UUID | None = None
    qualification: str | None = None
    specialization: str | None = None
    joining_date: date | None = None

    subject_ids: list[UUID] | None = None


class TeacherUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    password: str | None = None

    department_id: UUID | None = None
    qualification: str | None = None
    specialization: str | None = None
    joining_date: date | None = None

    subject_ids: list[UUID] | None = None


class TeacherResponse(BaseModel):
    id: UUID
    user_id: UUID

    full_name: str
    email: EmailStr
    phone: str | None = None

    department_id: UUID | None = None
    qualification: str | None = None
    specialization: str | None = None
    joining_date: date | None = None
    institution_id: UUID | None = None

    subject_ids: list[UUID] | None = None

    class Config:
        from_attributes = True