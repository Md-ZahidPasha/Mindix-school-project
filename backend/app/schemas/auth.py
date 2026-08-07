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
# Parent Login
# ==========================================
class ParentLoginRequest(BaseModel):
    student_id: str
    parent_phone: str


# ==========================================
# JWT Token
# ==========================================
class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"