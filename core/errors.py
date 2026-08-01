"""Custom exception types + Flask error handler registration.

Services/repositories raise these; controllers don't need to know
about HTTP status codes, they just let these propagate and the
handlers registered here turn them into JSON responses.
"""
from flask import jsonify


class AppError(Exception):
    status_code = 500
    code = "internal_error"

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message or self.code


class NotFoundError(AppError):
    status_code = 404
    code = "not_found"


class ValidationError(AppError):
    status_code = 400
    code = "validation_error"


class UnauthorizedError(AppError):
    status_code = 401
    code = "unauthorized"


class UpstreamServiceError(AppError):
    """Raised when an adapter (LLM, embeddings, vector store, catalog
    feed) fails. Kept distinct from AppError so callers can decide to
    retry/fallback differently than on a plain validation problem."""

    status_code = 502
    code = "upstream_service_error"


def register_error_handlers(app):
    @app.errorhandler(AppError)
    def handle_app_error(err):
        return jsonify({"error": err.code, "message": err.message}), err.status_code

    @app.errorhandler(404)
    def handle_404(_err):
        return jsonify({"error": "not_found", "message": "Not found"}), 404

    @app.errorhandler(405)
    def handle_405(_err):
        return jsonify({"error": "method_not_allowed", "message": "Method not allowed"}), 405

    @app.errorhandler(500)
    def handle_500(_err):
        return jsonify({"error": "internal_error", "message": "Internal server error"}), 500
