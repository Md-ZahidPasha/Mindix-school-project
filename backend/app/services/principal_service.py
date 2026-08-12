from uuid import UUID

from sqlalchemy.orm import Session

from app.models.principal import Principal
from app.models.user import User
from app.schemas.principal import PrincipalCreate
from app.core.security import hash_password


def create_principal(
    db: Session,
    principal_data: PrincipalCreate
):
    # Check whether email already exists
    existing_user = (
        db.query(User)
        .filter(User.email == principal_data.email)
        .first()
    )

    if existing_user:
        raise ValueError(
            "A user with this email already exists"
        )

    # Check whether Principal ID already exists
    existing_principal = (
        db.query(Principal)
        .filter(
            Principal.principal_id
            == principal_data.principal_id
        )
        .first()
    )

    if existing_principal:
        raise ValueError(
            "A principal with this Principal ID already exists"
        )

    # Create user account
    user = User(
        institution_id=principal_data.institution_id,
        full_name=principal_data.full_name,
        email=principal_data.email,
        phone=principal_data.phone,
        password_hash=hash_password(
            principal_data.password
        ),
        role="principal",
        status="active",
    )

    db.add(user)
    db.flush()

    # Create Principal profile
    principal = Principal(
        user_id=user.id,
        principal_id=principal_data.principal_id,
        qualification=principal_data.qualification,
        experience_years=principal_data.experience_years,
        date_of_birth=principal_data.date_of_birth,
        gender=principal_data.gender,
        institution_id=principal_data.institution_id,
    )

    db.add(principal)

    db.commit()

    db.refresh(principal)
    db.refresh(user)

    return principal, user