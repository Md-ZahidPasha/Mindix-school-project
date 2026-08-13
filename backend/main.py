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


app = FastAPI(
    title="PaperBuddy API",
    description="AI Powered School Operations Platform",
    version="1.0.0"
)


# ============================================================
# CORS CONFIGURATION
# ============================================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
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


# ============================================================
# ROOT
# ============================================================

@app.get("/")
def root():
    return {
        "message": "Welcome to PaperBuddy API 🚀"
    }