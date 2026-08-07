from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.institution import router as institution_router
from app.api.auth import router as auth_router
from app.api.dashboard import router as dashboard_router

app = FastAPI(
    title="PaperBuddy API",
    description="AI Powered School Operations Platform",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later restrict this to your frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(health_router)
app.include_router(institution_router)
app.include_router(auth_router)
app.include_router(dashboard_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to PaperBuddy API 🚀"
    }