from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.health import router as health_router

app = FastAPI(
    title="PaperBuddy API",
    description="AI Powered School Operations Platform",
    version="1.0.0"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Later we'll replace * with the frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(health_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to PaperBuddy API 🚀"
    }