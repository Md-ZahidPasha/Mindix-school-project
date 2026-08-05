from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()


class Settings:
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_ANON_KEY = os.getenv("SUPABASE_ANON_KEY")
    DATABASE_URL = os.getenv("DATABASE_URL")
    SECRET_KEY = os.getenv("SECRET_KEY")
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")


settings = Settings()