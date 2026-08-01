"""Entry point for POST /api/v1/chat. Wires together: rewrite -> intent
-> retrieval (fusion+rerank) -> generation (prompt+llm+validate) ->
memory, and logs the turn via services/analytics/query_log.

This is the file to read first to understand the whole chat pipeline;
every stage below it is replaceable independently (see the module
docstrings in retrieval/, generation/, and adapters/).
"""
import time

from services.chat import intent, rewrite, memory
from services.retrieval import fusion, rerank
from services.generation import prompt_builder, llm_client, validator
from repositories.announcement_repository import AnnouncementRepository
from services.analytics import query_log

_announcements_repo = AnnouncementRepository()


def handle_message(text: str, conversation_id=None):
    started = time.perf_counter()

    conversation = memory.get_or_create(conversation_id, seed_title=text)
    clean_text = rewrite.rewrite(text, memory.history(conversation.id))
    detected_intent = intent.classify(clean_text)

    books = []
    announcements = []

    if detected_intent == intent.INTENT_ANNOUNCEMENTS:
        announcements = [a.message for a in _announcements_repo.list()]
    else:
        candidates = fusion.retrieve(clean_text)
        books = rerank.rerank(clean_text, candidates)

    system_prompt, drafted_reply = prompt_builder.build(clean_text, books, announcements)
    reply_text = validator.validate(llm_client.generate(system_prompt, drafted_reply))

    memory.record_turn(conversation.id, text, reply_text)

    latency_ms = int((time.perf_counter() - started) * 1000)
    query_log.record(
        text,
        conversation_id=conversation.id,
        intent=detected_intent,
        result_count=len(books),
        latency_ms=latency_ms,
    )

    return {
        "conversation_id": conversation.id,
        "reply": reply_text,
        "books": [b.to_dict() for b in books[:4]],
        "announcements": announcements,
        "intent": detected_intent,
    }
