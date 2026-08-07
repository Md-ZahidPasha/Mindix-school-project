from sqlalchemy.orm import Session

from app.models.institution import Institution
from app.schemas.auth import (
    InstitutionLoginRequest,
    InstitutionLoginResponse,
)
from app.core.security import (
    verify_password,
    create_access_token,
)


def login_institution(
    db: Session,
    login_data: InstitutionLoginRequest,
):
    institution = (
        db.query(Institution)
        .filter(
            Institution.institution_name == login_data.institution_name
        )
        .first()
    )

    if not institution:
        return None

    if not verify_password(
        login_data.password,
        institution.password_hash,
    ):
        return None

    access_token = create_access_token(
        data={
            "institution_id": str(institution.id),
            "institution_name": institution.institution_name,
            "role": "admin",
        }
    )

    return InstitutionLoginResponse(
        message="Login successful",
        institution_id=str(institution.id),
        institution_name=institution.institution_name,
        user_id=str(institution.id),  # Temporary until users table login is implemented
        role="admin",
        access_token=access_token,
        token_type="bearer",
    )