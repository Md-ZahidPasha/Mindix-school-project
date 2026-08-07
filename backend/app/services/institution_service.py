from sqlalchemy.orm import Session

from app.models.institution import Institution
from app.schemas.auth import InstitutionCreateRequest
from app.core.security import hash_password


def get_institution_by_name(db: Session, institution_name: str):
    return (
        db.query(Institution)
        .filter(Institution.institution_name == institution_name)
        .first()
    )


def get_institution_by_email(db: Session, email: str):
    return (
        db.query(Institution)
        .filter(Institution.email == email)
        .first()
    )


def create_institution(db: Session, institution: InstitutionCreateRequest):
    new_institution = Institution(
        institution_name=institution.institution_name,
        institution_type=institution.institution_type,
        email=institution.email,
        phone=institution.phone,
        password_hash=hash_password(institution.password),
        status="active"
    )

    db.add(new_institution)
    db.commit()
    db.refresh(new_institution)

    return new_institution