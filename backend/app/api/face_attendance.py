from datetime import date
from uuid import UUID

from fastapi import APIRouter, Depends, File, Form, HTTPException, UploadFile
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.core.security import decode_access_token
from app.database.session import get_db
from app.schemas.attendance import AttendanceCreate
from app.services.attendance_service import create_attendance
from app.services.face_attendance_service import face_embedding, find_face_match, save_face_profile

router = APIRouter(prefix="/api/attendance/face", tags=["Face Attendance"])
security = HTTPBearer()


def require_staff(credentials: HTTPAuthorizationCredentials = Depends(security)):
    user = decode_access_token(credentials.credentials)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid or expired authentication token.")
    if (user.get("role") or "").lower() not in {"admin", "principal", "teacher", "staff"}:
        raise HTTPException(status_code=403, detail="Staff authorization is required.")
    return user


@router.post("/enroll")
async def enroll_face(student_id: UUID = Form(...), institution_id: UUID = Form(...), file: UploadFile = File(...), db: Session = Depends(get_db), _: dict = Depends(require_staff)):
    try:
        embedding = face_embedding(await file.read())
        save_face_profile(db, student_id, institution_id, embedding)
        return {"status": "enrolled", "student_id": str(student_id), "message": "Face profile enrolled successfully."}
    except ValueError as error:
        raise HTTPException(status_code=422, detail=str(error)) from error


@router.post("/recognize")
async def recognize_and_mark(institution_id: UUID = Form(...), class_id: UUID = Form(...), period_id: UUID | None = Form(None), attendance_date: date | None = Form(None), file: UploadFile = File(...), db: Session = Depends(get_db), current_user: dict = Depends(require_staff)):
    try:
        match = find_face_match(db, institution_id, face_embedding(await file.read()))
        attendance = create_attendance(db, AttendanceCreate(
            student_id=match["student_id"], class_id=class_id, period_id=period_id,
            institution_id=institution_id, teacher_id=current_user.get("teacher_id"),
            attendance_date=attendance_date or date.today(), status="present",
            attendance_type="student", attendance_mode="face",
        ))
        return {"status": "present", "student": match, "attendance_id": str(attendance.id)}
    except ValueError as error:
        detail = str(error)
        raise HTTPException(status_code=409 if "Already marked" in detail else 422, detail=detail) from error
