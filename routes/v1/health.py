from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def get_health():
    return jsonify({"status": "ok", "service": "ASKMQL API", "version": "v1"})
