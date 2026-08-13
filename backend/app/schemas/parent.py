from uuid import UUID

from pydantic import BaseModel, EmailStr


class ParentCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str

    # Human-readable student ID, e.g. STU001
    student_id: str

    institution_id: UUID


class ParentResponse(BaseModel):
    id: UUID
    parent_id: str
    user_id: UUID
    full_name: str
    email: EmailStr
    phone: str | None = None
    student_id: str
    institution_id: UUID

    class Config:
        from_attributes = True