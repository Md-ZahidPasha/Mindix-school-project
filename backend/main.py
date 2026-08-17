from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.institution import router as institution_router
from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router
from app.api.students import router as students_router
from app.api.principal import router as principal_router
from app.api.documents import router as documents_router
from app.api.ai import router as ai_router
from app.api.parent import router as parent_router
from app.api.employees import router as employees_router
from app.api.attendance import router as attendance_router
from app.api.tasks import router as tasks_router
from app.api.leave_applications import router as leave_applications_router
from app.api.timetable import router as timetable_router
from app.api.schedule import router as schedule_router
from app.api.face_attendance import router as face_attendance_router
from app.api.certificates import router as certificates_router
from app.api.library import router as library_router
from app.api.substitutions import router as substitutions_router
from app.api.teachers import router as teachers_router
import app.models  # Register every model with the single SQLAlchemy Base before use.
from app.core.config import settings


app = FastAPI(
    title="PaperBuddy API",
    description="AI Powered School Operations Platform",
    version="1.0.0"
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

allowed_origins = [
    "http://localhost:5173",
    "http://127.0.0.1:5173",
]
if settings.FRONTEND_URL:
    allowed_origins.extend(origin.strip() for origin in settings.FRONTEND_URL.split(",") if origin.strip())

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "DELETE",
        "OPTIONS",
    ],
    allow_headers=["*"],
)


# ============================================================
# ROUTERS
# ============================================================

app.include_router(health_router)
app.include_router(institution_router)
app.include_router(auth_router)
app.include_router(dashboard_router)
app.include_router(students_router)
app.include_router(principal_router)
app.include_router(documents_router)
app.include_router(ai_router)
app.include_router(parent_router)
app.include_router(employees_router)
app.include_router(attendance_router)
app.include_router(tasks_router)
app.include_router(leave_applications_router)
app.include_router(timetable_router)
app.include_router(schedule_router)
app.include_router(face_attendance_router)
app.include_router(certificates_router)
app.include_router(library_router)
app.include_router(substitutions_router)
app.include_router(teachers_router)

# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Welcome to PaperBuddy API 🚀"
    }
