"""Central app configuration, pulled from environment variables.

Defaults match a stock local XAMPP/MySQL setup (root user, no
password, default port 3306). Override with a .env file locally, or
real environment variables when deploying.
"""
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENV = os.environ.get("FLASK_ENV", "development")
    DEBUG = os.environ.get("FLASK_DEBUG", "1") == "1"
    PORT = int(os.environ.get("PORT", 5000))
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev-secret-change-me")

    DB_HOST = os.environ.get("DB_HOST", "localhost")
    DB_PORT = os.environ.get("DB_PORT", "3306")
    DB_USER = os.environ.get("DB_USER", "root")
    DB_PASSWORD = os.environ.get("DB_PASSWORD", "")
    DB_NAME = os.environ.get("DB_NAME", "askmql")

    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL",
        f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}",
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # A concrete origin is required (not "*") for the auth session
    # cookie to work cross-origin -- browsers won't send credentials
    # to a wildcard origin. Update for your deployed frontend URL.
    CORS_ORIGINS = os.environ.get("CORS_ORIGINS", "http://localhost:8000")

    # Session cookie (used by services/auth/auth_service.py). "Lax" is
    # fine when frontend+backend share a site; switch to "None" (and
    # SESSION_COOKIE_SECURE=1, which requires HTTPS) for a genuinely
    # cross-site deployment (e.g. Vercel frontend + Render backend).
    SESSION_COOKIE_SAMESITE = os.environ.get("SESSION_COOKIE_SAMESITE", "Lax")
    SESSION_COOKIE_SECURE = os.environ.get("SESSION_COOKIE_SECURE", "0") == "1"
    SESSION_COOKIE_HTTPONLY = True

    # ---- RAG / retrieval knobs (all currently backed by placeholder
    # adapters -- see adapters/llm, adapters/embeddings, adapters/vector) ----
    LLM_PROVIDER = os.environ.get("LLM_PROVIDER", "template")   # template | anthropic
    EMBEDDINGS_PROVIDER = os.environ.get("EMBEDDINGS_PROVIDER", "none")
    VECTOR_STORE = os.environ.get("VECTOR_STORE", "in_memory")
    RETRIEVAL_TOP_K = int(os.environ.get("RETRIEVAL_TOP_K", 4))

    AUTO_CREATE_TABLES = os.environ.get("AUTO_CREATE_TABLES", "0") == "1"
    LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")


def get_config():
    return Config
