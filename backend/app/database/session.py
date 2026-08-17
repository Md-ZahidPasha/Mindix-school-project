from sqlalchemy.orm import sessionmaker
from fastapi import HTTPException

from app.database.connection import engine

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)


def get_db():
    if engine is None:
        raise HTTPException(
            status_code=503,
            detail="DATABASE_URL is not configured. Configure the existing Supabase PostgreSQL connection.",
        )
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
