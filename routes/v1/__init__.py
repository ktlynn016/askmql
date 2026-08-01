"""v1 blueprint registry -- app.py imports register_v1_blueprints and
calls it once, rather than importing each blueprint individually."""
from routes.v1.health import health_bp
from routes.v1.auth import auth_bp
from routes.v1.chat import chat_bp
from routes.v1.books import books_bp
from routes.v1.availability import availability_bp
from routes.v1.announcements import announcements_bp
from routes.v1.conversations import conversations_bp
from routes.v1.feedback import feedback_bp
from routes.v1.admin import admin_bp

ALL_V1_BLUEPRINTS = [
    health_bp,
    auth_bp,
    chat_bp,
    books_bp,
    availability_bp,
    announcements_bp,
    conversations_bp,
    feedback_bp,
    admin_bp,
]


def register_v1_blueprints(app, url_prefix="/api/v1"):
    for bp in ALL_V1_BLUEPRINTS:
        app.register_blueprint(bp, url_prefix=url_prefix)
