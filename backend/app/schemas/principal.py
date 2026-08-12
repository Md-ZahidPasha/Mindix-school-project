from datetime import date
from uuid import UUID

from pydantic import BaseModel, EmailStr


class PrincipalCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    phone: str | None = None

    principal_id: str
    qualification: str | None = None
    experience_years: int | None = None
    date_of_birth: date | None = None
    gender: str | None = None

    institution_id: UUID


class PrincipalResponse(BaseModel):
    id: UUID
    user_id: UUID

    full_name: str
    email: EmailStr
    phone: str | None = None

    principal_id: str
    qualification: str | None = None
    experience_years: int | None = None
    date_of_birth: date | None = None
    gender: str | None = None
    institution_id: UUID

    class Config:
        from_attributes = True