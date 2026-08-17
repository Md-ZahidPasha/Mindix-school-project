from pydantic import BaseModel, EmailStr


# ==========================================
# Institution Registration
# ==========================================
class InstitutionCreateRequest(BaseModel):
    institution_name: str
    institution_type: str
    admin_name: str
    email: EmailStr
    phone: str
    password: str


# ==========================================
# Institution Registration Response
# ==========================================
class InstitutionCreateResponse(BaseModel):
    message: str
    institution_id: str
    institution_name: str


# ==========================================
# Institution Login
# ==========================================
class InstitutionLoginRequest(BaseModel):
    institution_name: str
    password: str


# ==========================================
# Institution Login Response
# ==========================================
class InstitutionLoginResponse(BaseModel):
    message: str
    institution_id: str
    institution_name: str
    user_id: str
    role: str
    access_token: str
    token_type: str = "bearer"


# ==========================================
# Student Login
# ==========================================
class StudentLoginRequest(BaseModel):
    student_id: str
    password: str


# ==========================================
# Student Login Response
# ==========================================
class StudentLoginResponse(BaseModel):
    message: str
    student_id: str
    user_id: str
    institution_id: str
    role: str
    full_name: str
    access_token: str
    token_type: str = "bearer"


# ==========================================
# Parent Login
# ==========================================
class ParentLoginRequest(BaseModel):
    parent_id: str
    password: str


# ==========================================
# Parent Login Response
# ==========================================
class ParentLoginResponse(BaseModel):
    message: str
    parent_id: str
    user_id: str
    institution_id: str
    role: str
    full_name: str
    access_token: str
    token_type: str = "bearer"

# ==========================================
# Staff / Employee Login
# ==========================================
class StaffLoginRequest(BaseModel):
    institution_name: str
    email: str
    password: str


class StaffLoginResponse(BaseModel):
    message: str
    user_id: str
    institution_id: str
    role: str
    full_name: str
    access_token: str
    token_type: str = "bearer"
    employee_id: str | None = None
    teacher_id: str | None = None


# ==========================================
# JWT Token
# ==========================================
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"