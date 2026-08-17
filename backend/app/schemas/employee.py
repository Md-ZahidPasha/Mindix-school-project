from datetime import date
from uuid import UUID

from pydantic import BaseModel, EmailStr


class EmployeeCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str

    designation: str | None = None
    department_id: UUID | None = None
    joining_date: date | None = None
    institution_id: UUID | None = None

    employee_code: str | None = None
    alternate_phone: str | None = None
    employment_type: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    pincode: str | None = None


class EmployeeUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None

    designation: str | None = None
    department_id: UUID | None = None
    joining_date: date | None = None
    institution_id: UUID | None = None

    employee_code: str | None = None
    alternate_phone: str | None = None
    employment_type: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    pincode: str | None = None


class EmployeeResponse(BaseModel):
    id: UUID
    user_id: UUID

    full_name: str
    email: EmailStr
    phone: str | None = None

    designation: str | None = None
    department_id: UUID | None = None
    joining_date: date | None = None
    institution_id: UUID | None = None

    employee_code: str | None = None
    alternate_phone: str | None = None
    employment_type: str | None = None
    address: str | None = None
    city: str | None = None
    state: str | None = None
    pincode: str | None = None

    class Config:
        from_attributes = True