from fastapi import FastAPI

app = FastAPI(
    title="PaperBuddy API",
    description="AI Powered School Operations Platform",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to PaperBuddy API 🚀"
    }