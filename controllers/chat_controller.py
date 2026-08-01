from flask import jsonify, request

from services.chat import orchestrator
from core.errors import ValidationError


def post_chat():
    data = request.get_json(silent=True) or {}
    text = (data.get("message") or "").strip()
    conversation_id = data.get("conversation_id")

    if not text:
        raise ValidationError("message is required")

    result = orchestrator.handle_message(text, conversation_id=conversation_id)
    return jsonify(result)
