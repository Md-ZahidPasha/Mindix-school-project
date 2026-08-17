from datetime import date, datetime, timezone
from uuid import UUID

from sqlalchemy import text
from sqlalchemy.orm import Session

from app.models.certificate import Certificate
from app.schemas.certificate import CertificateCreate, CertificateStatusUpdate

CERT_STATUSES = {"pending", "approved", "rejected", "issued"}


def _row_to_response(row) -> dict:
    r = dict(row)
    r["id"] = r.get("id")
    return r


def create_certificate(db: Session, data: CertificateCreate, requested_by: UUID):
    certificate = Certificate(
        student_id=data.student_id,
        institution_id=data.institution_id,
        certificate_name=data.certificate_name,
        certificate_type=data.certificate_type,
        purpose=data.purpose,
        status="pending",
        requested_by=requested_by,
    )
    db.add(certificate)
    db.commit()
    db.refresh(certificate)
    return certificate


def list_certificates(db: Session, institution_id: UUID, status: str | None = None, student_id: UUID | None = None):
    sql = """
        SELECT c.*,
               u.full_name AS student_name,
               s.roll_number AS student_roll,
               cls.class_name,
               s.student_id AS student_code
        FROM certificates c
        JOIN students s ON s.id = c.student_id
        LEFT JOIN users u ON u.id = s.user_id
        LEFT JOIN classes cls ON cls.id = s.class_id
        WHERE c.institution_id = :iid
    """
    params: dict = {"iid": str(institution_id)}
    if status:
        sql += " AND c.status = :status"
        params["status"] = status
    if student_id:
        sql += " AND c.student_id = :sid"
        params["sid"] = str(student_id)
    sql += " ORDER BY c.created_at DESC"
    rows = db.execute(text(sql), params).mappings().all()
    return [_row_to_response(r) for r in rows]


def get_certificate(db: Session, institution_id: UUID, certificate_id: UUID):
    sql = """
        SELECT c.*,
               u.full_name AS student_name,
               s.roll_number AS student_roll,
               s.student_id AS student_code,
               s.class_id,
               s.date_of_birth,
               s.gender,
               cls.class_name,
               i.institution_name
        FROM certificates c
        JOIN students s ON s.id = c.student_id
        LEFT JOIN users u ON u.id = s.user_id
        LEFT JOIN classes cls ON cls.id = s.class_id
        LEFT JOIN institutions i ON i.id = c.institution_id
        WHERE c.institution_id = :iid AND c.id = :cid
    """
    row = db.execute(
        text(sql), {"iid": str(institution_id), "cid": str(certificate_id)}
    ).mappings().first()
    return _row_to_response(row) if row else None


def update_certificate_status(
    db: Session,
    institution_id: UUID,
    certificate_id: UUID,
    data: CertificateStatusUpdate,
    reviewer_user_id: UUID,
):
    certificate = (
        db.query(Certificate)
        .filter(
            Certificate.id == certificate_id,
            Certificate.institution_id == institution_id,
        )
        .first()
    )
    if not certificate:
        return None

    if certificate.status not in CERT_STATUSES:
        raise ValueError("Invalid certificate status.")

    certificate.status = data.status.lower()
    if data.status.lower() == "rejected":
        certificate.rejection_reason = data.rejection_reason
    if data.status.lower() in {"approved", "issued"}:
        certificate.approved_by = reviewer_user_id
        certificate.reviewed_at = datetime.now(timezone.utc)
        certificate.certificate_number = data.certificate_number or _generate_number(certificate.id)
        certificate.issue_date = data.issue_date or date.today()

    db.commit()
    db.refresh(certificate)
    return certificate


def _generate_number(certificate_id: UUID) -> str:
    return f"PB-{date.today().strftime('%Y%m%d')}-{str(certificate_id).split('-')[0].upper()}"