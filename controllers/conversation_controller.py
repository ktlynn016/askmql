from flask import jsonify, request

from repositories.conversation_repository import ConversationRepository
from core.errors import NotFoundError

_repo = ConversationRepository()


def get_conversations():
    return jsonify([c.to_dict() for c in _repo.list()])


def post_conversation():
    data = request.get_json(silent=True) or {}
    conv = _repo.create(data.get("title", "New conversation"))
    return jsonify(conv.to_dict()), 201


def patch_conversation(conversation_id):
    data = request.get_json(silent=True) or {}
    conv = _repo.rename(conversation_id, data.get("title"))
    if not conv:
        raise NotFoundError("Conversation not found")
    return jsonify(conv.to_dict())


def delete_conversation(conversation_id):
    ok = _repo.delete(conversation_id)
    if not ok:
        raise NotFoundError("Conversation not found")
    return "", 204


def get_messages(conversation_id):
    conv = _repo.get(conversation_id)
    if not conv:
        raise NotFoundError("Conversation not found")
    return jsonify([m.to_dict() for m in _repo.messages(conversation_id)])
