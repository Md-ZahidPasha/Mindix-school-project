from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from app.core.security import decode_access_token
from app.schemas.timetable import TimetableGenerateRequest, TimetableSlotResponse
from app.services.timetable_service import generate_timetable

router = APIRouter(prefix="/api/timetable", tags=["Timetable"])
security = HTTPBearer()


def require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if (user.get("role") or "").lower() not in {"admin", "principal", "teacher", "staff"}:
        raise HTTPException(status_code=403, detail="Only school staff can generate timetables.")
    return user


@router.post("/generate", response_model=list[TimetableSlotResponse])
def generate(request: TimetableGenerateRequest, _: dict = Depends(require_staff)):
    try:
        return generate_timetable(request)
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error
