"""Lightweight request timing middleware.

Logs method/path/status/duration for every request and stamps the
response with an X-Response-Time-Ms header. Also the natural place to
later emit these as metrics (see services/analytics/metrics.py).
"""
import time

from flask import request, g

from core.logging import get_logger

logger = get_logger("askmql.timing")


def configure_timing(app):
    @app.before_request
    def start_timer():
        g._start_time = time.perf_counter()

    @app.after_request
    def stop_timer(response):
        started = getattr(g, "_start_time", None)
        if started is not None:
            duration_ms = (time.perf_counter() - started) * 1000
            response.headers["X-Response-Time-Ms"] = f"{duration_ms:.1f}"
            logger.info(
                "%s %s -> %s (%.1fms)",
                request.method,
                request.path,
                response.status_code,
                duration_ms,
            )
        return response
