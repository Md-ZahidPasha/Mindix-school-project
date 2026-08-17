from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.models.user import User
from app.schemas.substitution import (
    SubstitutionCreate,
    SubstitutionResponse,
    SubstituteSuggestion,
    SubstituteSuggestionRequest,
)
from app.services.substitution_service import (
    confirm_substitution,
    delete_substitution,
    get_substitution,
    list_substitutions,
    suggest_substitutes,
)

router = APIRouter(prefix="/api/substitutions", tags=["Smart Substitution"])
security = HTTPBearer()

STAFF_ROLES = {"admin", "principal", "teacher", "staff"}


def _require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)) -> dict:
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if not user.get("institution_id"):
        raise HTTPException(status_code=401, detail="Token is missing the institution scope.")
    if (user.get("role") or "").lower() not in STAFF_ROLES:
        raise HTTPException(status_code=403, detail="Staff authorization is required.")
    return user


@router.post("/suggest", response_model=list[SubstituteSuggestion])
def suggest(
    data: SubstituteSuggestionRequest,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    try:
        suggestions = suggest_substitutes(db, UUID(user["institution_id"]), data.leave_application_id)
    except ValueError as error:
        raise HTTPException(status_code=404, detail=str(error))
    return suggestions


@router.post("", response_model=SubstitutionResponse, status_code=status.HTTP_201_CREATED)
def create_substitution(
    data: SubstitutionCreate,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    reviewer = None
    user_id = user.get("user_id")
    if user_id:
        try:
            candidate = UUID(user_id)
            if db.query(User.id).filter(User.id == candidate).first():
                reviewer = candidate
        except ValueError:
            pass
    substitution = confirm_substitution(db, UUID(user["institution_id"]), data, reviewer)
    return get_substitution(db, UUID(user["institution_id"]), substitution.id)


@router.get("", response_model=list[SubstitutionResponse])
def list_substitutions_endpoint(
    status_filter: str | None = None,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    return list_substitutions(db, UUID(user["institution_id"]), status=status_filter)


@router.get("/{substitution_id}", response_model=SubstitutionResponse)
def get_substitution_endpoint(
    substitution_id: UUID,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    substitution = get_substitution(db, UUID(user["institution_id"]), substitution_id)
    if not substitution:
        raise HTTPException(status_code=404, detail="Substitution not found.")
    return substitution


@router.delete("/{substitution_id}")
def delete_substitution_endpoint(
    substitution_id: UUID,
    user: dict = Depends(_require_staff),
    db: Session = Depends(get_db),
):
    deleted = delete_substitution(db, UUID(user["institution_id"]), substitution_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Substitution not found.")
    return {"status": "success", "message": "Substitution removed."}