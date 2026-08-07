from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

from app.core.config import settings

# SQLAlchemy Engine
engine = create_engine(
    settings.DATABASE_URL,
    pool_pre_ping=True
)

# Base class for all SQLAlchemy models
Base = declarative_base()