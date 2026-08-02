"""ASKMQL backend -- application factory only. Actual startup lives in
wsgi.py (or the __main__ block below for local dev).

Layout:
    core/        config, logging, error handling, CORS/admin auth, timing
    routes/v1/   URL -> controller wiring (Blueprints)
    controllers/ request/response glue
    services/    chat pipeline, retrieval, generation, catalog, analytics
    repositories/ data access (wraps SQLAlchemy models)
    adapters/    swappable integrations: llm, embeddings, vector, catalog feed
    jobs/        sync_catalog, refresh_embeddings (run manually or on a schedule)
"""
from flask import Flask

from core.config import Config
from core.logging import configure_logging
from core.errors import register_error_handlers
from core.security import configure_cors
from core.timing import configure_timing
from database.db import db
from routes.v1 import register_v1_blueprints


def create_app():
    configure_logging(Config.LOG_LEVEL)

    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    configure_cors(app)
    configure_timing(app)
    register_error_handlers(app)
    register_v1_blueprints(app)

    if Config.AUTO_CREATE_TABLES:
        with app.app_context():
            db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=Config.DEBUG, port=Config.PORT)
