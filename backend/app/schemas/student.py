from datetime import date
from uuid import UUID

from pydantic import BaseModel, EmailStr


class StudentCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str | None = None

    roll_number: str
    admission_number: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    class_id: UUID | None = None
    institution_id: UUID


class StudentUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

    roll_number: str | None = None
    admission_number: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    class_id: UUID | None = None


class StudentResponse(BaseModel):
    id: UUID
    user_id: UUID
    full_name: str
    email: EmailStr
    phone: str | None = None

    roll_number: str
    admission_number: str | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    class_id: UUID | None = None
    institution_id: UUID | None = None

    class Config:
        from_attributes = True