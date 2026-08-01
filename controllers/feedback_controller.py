from flask import jsonify, request

from services.analytics import feedback as feedback_service


def post_feedback():
    data = request.get_json(silent=True) or {}
    item = feedback_service.submit(
        data.get("message_id"), data.get("rating"), note=data.get("note")
    )
    return jsonify(item.to_dict()), 201
