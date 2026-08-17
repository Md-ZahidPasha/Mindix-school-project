from dotenv import load_dotenv
import os

load_dotenv()


class Settings:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    SUPABASE_SERVICE_ROLE_KEY = os.getenv("SUPABASE_SERVICE_ROLE_KEY")
    # PaperBuddy always uses the existing Supabase/PostgreSQL database.
    # A missing value is handled by the database dependency; it never falls
    # back to a local/demo database.
    DATABASE_URL = os.getenv("DATABASE_URL")

    SECRET_KEY = os.getenv("JWT_SECRET") or os.getenv("SECRET_KEY", "change-this-before-production")

    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 60

    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
    GEMINI_MODEL = os.getenv("GEMINI_MODEL", "gemini-2.5-flash")
    FRONTEND_URL = os.getenv("FRONTEND_URL", "")


settings = Settings()
