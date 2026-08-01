"""CORS setup + session-based auth guards.

Login state lives entirely in Flask's signed, httpOnly session cookie
(set via services/auth/auth_service.py) -- never in client-side JS
storage of any kind. `login_required` and `require_role` are what
routes/controllers use to gate access; services/auth/auth_service.py
is what actually authenticates a request.
"""
from functools import wraps

from flask import session
from flask_cors import CORS

from core.config import Config
from core.errors import UnauthorizedError


def configure_cors(app):
    # supports_credentials=True is required for the session cookie to
    # be sent/received cross-origin (frontend and backend on
    # different ports/domains). Browsers reject credentialed requests
    # against a wildcard origin, so CORS_ORIGINS must be a concrete
    # origin (or comma-separated list) once auth is in use -- see
    # .env.example.
    CORS(
        app,
        resources={r"/api/*": {"origins": Config.CORS_ORIGINS}},
        supports_credentials=True,
    )


def login_required(view_func):
    @wraps(view_func)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            raise UnauthorizedError("Login required")
        return view_func(*args, **kwargs)

    return wrapped


def require_role(role_name):
    def decorator(view_func):
        @wraps(view_func)
        def wrapped(*args, **kwargs):
            if not session.get("user_id"):
                raise UnauthorizedError("Login required")
            if session.get("role") != role_name:
                raise UnauthorizedError(f"Requires {role_name} role")
            return view_func(*args, **kwargs)

        return wrapped

    return decorator
