from uuid import UUID

from pydantic import BaseModel, EmailStr


# ==========================================
# Create Parent
# ==========================================
class ParentCreate(BaseModel):
    full_name: str
    email: EmailStr
    phone: str | None = None
    password: str

    # Student to link initially
    # Example: STU001
    student_id: str

    institution_id: UUID


# ==========================================
# Update Parent
# ==========================================
class ParentUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None


# ==========================================
# Student linked to Parent
# ==========================================
class ParentStudentResponse(BaseModel):
    student_id: str
    full_name: str
    roll_number: str
    admission_number: str | None = None


# ==========================================
# Parent Response
# ==========================================
class ParentResponse(BaseModel):
    id: UUID
    parent_id: str
    user_id: UUID

    full_name: str
    email: EmailStr
    phone: str | None = None

    institution_id: UUID

    students: list[ParentStudentResponse] = []

    class Config:
        from_attributes = True


# ==========================================
# Add Student to Existing Parent
# ==========================================
class ParentStudentCreate(BaseModel):
    student_id: str