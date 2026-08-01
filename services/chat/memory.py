"""Conversation memory helpers -- thin wrapper over
ConversationRepository so the orchestrator doesn't touch the
repository layer directly. Also the natural place to later add
summarization once conversations get long."""
from repositories.conversation_repository import ConversationRepository

_repo = ConversationRepository()


def get_or_create(conversation_id, seed_title=None):
    return _repo.get_or_create(conversation_id, seed_title=seed_title)


def record_turn(conversation_id, user_text, ai_text):
    _repo.add_message(conversation_id, "user", user_text)
    ai_message = _repo.add_message(conversation_id, "ai", ai_text)
    return ai_message


def history(conversation_id):
    return _repo.messages(conversation_id)
