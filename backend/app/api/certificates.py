from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.user import User
from app.models.student import Student
from app.schemas.certificate import (
    CertificateCreate,
    CertificateResponse,
    CertificateStatusUpdate,
)
from app.services.certificate_service import (
    create_certificate,
    get_certificate,
    list_certificates,
    update_certificate_status,
)

router = APIRouter(prefix="/api/certificates", tags=["Certificates"])
security = HTTPBearer()

STAFF_ROLES = {"admin", "principal", "teacher", "staff"}


def _get_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if not user.get("institution_id"):
        raise HTTPException(status_code=401, detail="Token is missing the institution scope.")
    return user


def _require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = _get_user(credentials)
    if (user.get("role") or "").lower() not in STAFF_ROLES:
        raise HTTPException(status_code=403, detail="Staff authorization is required.")
    return user


def _real_user_id(db: Session, user: dict) -> UUID | None:
    user_id = user.get("user_id")
    if not user_id:
        return None
    try:
        candidate = UUID(user_id)
    except ValueError:
        return None
    exists = db.query(User.id).filter(User.id == candidate).first()
    return candidate if exists else None


@router.post("", response_model=CertificateResponse, status_code=status.HTTP_201_CREATED)
def create_certificate_request(
    data: CertificateCreate,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    institution_id = user["institution_id"]
    if data.institution_id is not None and str(data.institution_id) != str(institution_id):
        raise HTTPException(status_code=403, detail="Institution scope mismatch.")
    data.institution_id = UUID(institution_id)
    if (user.get("role") or "").lower() == "student":
        sid = user.get("student_id")
        if not sid:
            raise HTTPException(status_code=403, detail="Student token is missing student scope.")
        student = (
            db.query(Student)
            .filter(
                Student.student_id == sid,
                Student.institution_id == user.get("institution_id"),
            )
            .first()
        )
        if not student:
            raise HTTPException(status_code=403, detail="Student scope is missing from the token.")
        data.student_id = student.id
    cert = create_certificate(db, data, _real_user_id(db, user))
    return get_certificate(db, UUID(institution_id), cert.id)


@router.get("", response_model=list[CertificateResponse])
def list_certificate_requests(
    status_filter: str | None = None,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    institution_id = UUID(user["institution_id"])
    student_id = None
    if (user.get("role") or "").lower() == "student":
        sid = user.get("student_id")
        if not sid:
            raise HTTPException(status_code=403, detail="Student token is missing student scope.")
        student = (
            db.query(Student)
            .filter(
                Student.student_id == sid,
                Student.institution_id == institution_id,
            )
            .first()
        )
        student_id = student.id if student else None
    return list_certificates(db, institution_id, status=status_filter, student_id=student_id)


@router.get("/{certificate_id}", response_model=CertificateResponse)
def get_certificate_request(
    certificate_id: UUID,
    user: dict = Depends(_get_user),
    db: Session = Depends(get_db),
):
    cert = get_certificate(db, UUID(user["institution_id"]), certificate_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate request not found.")
    return cert


@router.put("/{certificate_id}/status", response_model=CertificateResponse)
def review_certificate_request(
    certificate_id: UUID,
    data: CertificateStatusUpdate,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    if data.status.lower() not in {"approved", "rejected", "issued"}:
        raise HTTPException(status_code=422, detail="Status must be approved, rejected or issued.")
    reviewer = _real_user_id(db, user)
    cert = update_certificate_status(db, UUID(user["institution_id"]), certificate_id, data, reviewer)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate request not found.")
    return get_certificate(db, UUID(user["institution_id"]), certificate_id)