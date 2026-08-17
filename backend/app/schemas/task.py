from datetime import date, time, datetime
from uuid import UUID

from pydantic import BaseModel


class TaskCreate(BaseModel):
    title: str
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    status: str | None = None
    due_date: date | None = None
    due_time: time | None = None
    location: str | None = None

    employee_id: UUID
    department_id: UUID | None = None
    assigned_by: UUID
    institution_id: UUID


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    status: str | None = None
    due_date: date | None = None
    due_time: time | None = None
    location: str | None = None

    employee_id: UUID | None = None
    department_id: UUID | None = None


class TaskResponse(BaseModel):
    id: UUID
    title: str
    description: str | None = None
    category: str | None = None
    priority: str | None = None
    status: str | None = None
    due_date: date | None = None
    due_time: time | None = None
    location: str | None = None

    employee_id: UUID
    department_id: UUID | None = None
    assigned_by: UUID
    institution_id: UUID

    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True