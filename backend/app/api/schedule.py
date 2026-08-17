from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.schemas.schedule import (
    ScheduleConflictResponse,
    ScheduleEntryCreate,
    ScheduleEntryResponse,
    ScheduleEntryUpdate,
    ScheduleGenerateRequest,
    ScheduleGenerateResponse,
    ScheduleClass,
    ScheduleTeacher,
    ScheduleSubject,
)
from app.services.schedule_service import (
    create_schedule_entry,
    delete_schedule_entry,
    detect_conflicts,
    generate_schedule,
    list_classes,
    list_schedule_entries,
    list_subjects,
    list_teachers,
    update_schedule_entry,
)

router = APIRouter(prefix="/api/schedule", tags=["Schedule / Timetable"])
security = HTTPBearer()

STAFF_ROLES = {"admin", "principal", "teacher", "staff"}


def get_current_staff(
    credentials: HTTPAuthorizationCredentials = Depends(security),
) -> dict:
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
        )
    if (user.get("role") or "").lower() not in STAFF_ROLES:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only school staff can manage timetables.",
        )
    if not user.get("institution_id"):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token is missing the institution scope.",
        )
    return user


def _scope(user: dict, institution_id: UUID | None = None) -> str:
    token_institution = str(user["institution_id"])
    if institution_id is not None and str(institution_id) != token_institution:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only access your own institution's timetable.",
        )
    return token_institution


# ==========================================
# Lookup data
# ==========================================
@router.get("/classes", response_model=list[ScheduleClass])
def schedule_classes(
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    return list_classes(db, _scope(user))


@router.get("/teachers", response_model=list[ScheduleTeacher])
def schedule_teachers(
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    return list_teachers(db, _scope(user))


@router.get("/subjects", response_model=list[ScheduleSubject])
def schedule_subjects(
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    return list_subjects(db, _scope(user))


# ==========================================
# List / view
# ==========================================
@router.get("", response_model=list[ScheduleEntryResponse])
def list_schedule(
    class_id: UUID | None = Query(default=None),
    teacher_id: UUID | None = Query(default=None),
    day: str | None = Query(default=None),
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    institution_id = _scope(user)
    return list_schedule_entries(
        db,
        institution_id,
        class_id=class_id,
        teacher_id=teacher_id,
        day=day,
    )


@router.get("/class/{class_id}", response_model=list[ScheduleEntryResponse])
def schedule_for_class(
    class_id: UUID,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    return list_schedule_entries(db, _scope(user), class_id=class_id)


@router.get("/teacher/{teacher_id}", response_model=list[ScheduleEntryResponse])
def schedule_for_teacher(
    teacher_id: UUID,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    return list_schedule_entries(db, _scope(user), teacher_id=teacher_id)


# ==========================================
# Conflict detection
# ==========================================
@router.get("/conflicts", response_model=ScheduleConflictResponse)
def schedule_conflicts(
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    institution_id = _scope(user)
    return ScheduleConflictResponse(
        institution_id=UUID(institution_id),
        conflicts=detect_conflicts(db, institution_id),
    )


# ==========================================
# Generation (OR-Tools over real database records)
# ==========================================
@router.post("/generate", response_model=ScheduleGenerateResponse)
def schedule_generate(
    request: ScheduleGenerateRequest,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    try:
        return generate_schedule(db, _scope(user), request)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        ) from error


# ==========================================
# CRUD
# ==========================================
@router.post("", response_model=ScheduleEntryResponse, status_code=status.HTTP_201_CREATED)
def schedule_create(
    data: ScheduleEntryCreate,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    try:
        return create_schedule_entry(db, _scope(user), data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT if "conflict" in str(error).lower()
            else status.HTTP_422_UNPROCESSABLE_ENTITY,
            detail=str(error),
        ) from error


@router.put("/{entry_id}", response_model=ScheduleEntryResponse)
def schedule_update(
    entry_id: UUID,
    data: ScheduleEntryUpdate,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    try:
        return update_schedule_entry(db, _scope(user), entry_id, data)
    except ValueError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
            if "not found" in str(error).lower()
            else status.HTTP_409_CONFLICT,
            detail=str(error),
        ) from error


@router.delete("/{entry_id}")
def schedule_delete(
    entry_id: UUID,
    user: dict = Depends(get_current_staff),
    db: Session = Depends(get_db),
):
    deleted = delete_schedule_entry(db, _scope(user), entry_id)
    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Schedule entry not found.",
        )
    return {"status": "success", "message": "Schedule entry deleted successfully."}