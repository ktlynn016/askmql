"""Admin endpoints: aggregate metrics + manual catalog sync trigger.
All routes here are wrapped with core.security.require_role("librarian")."""
from flask import jsonify

from services.analytics.metrics import summary
from jobs.sync_catalog import run as run_sync_catalog


def get_metrics():
    return jsonify(summary())


def post_sync_catalog():
    result = run_sync_catalog()
    return jsonify(result)
