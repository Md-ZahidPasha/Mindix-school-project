from datetime import date, datetime
from uuid import UUID

from pydantic import BaseModel, Field


class CertificateCreate(BaseModel):
    student_id: UUID | None = None
    institution_id: UUID | None = None
    certificate_name: str = Field(..., description="e.g. Bonafide, School Leaving, Character")
    certificate_type: str | None = None
    purpose: str | None = None


class CertificateUpdate(BaseModel):
    status: str | None = None
    rejection_reason: str | None = None
    certificate_number: str | None = None
    issue_date: date | None = None


class CertificateResponse(BaseModel):
    id: UUID
    student_id: UUID
    institution_id: UUID | None = None
    requested_by: UUID | None = None
    certificate_name: str
    certificate_type: str | None = None
    purpose: str | None = None
    status: str | None = None
    certificate_number: str | None = None
    approved_by: UUID | None = None
    rejection_reason: str | None = None
    issue_date: date | None = None
    reviewed_at: datetime | None = None
    created_at: datetime | None = None
    student_name: str | None = None
    student_roll: str | None = None
    class_name: str | None = None
    section: str | None = None
    institution_name: str | None = None

    model_config = {"from_attributes": True}


class CertificateStatusUpdate(BaseModel):
    status: str
    rejection_reason: str | None = None
    certificate_number: str | None = None
    issue_date: date | None = None