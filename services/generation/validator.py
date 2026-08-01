"""Minimal output guardrail: today just trims/normalizes whitespace
and enforces a max length so a future real LLM can't return something
absurdly long into the chat UI. Expand with citation/consistency
checks once real generation is wired up."""

_MAX_LEN = 2000


def validate(reply_text: str) -> str:
    text = (reply_text or "").strip()
    if len(text) > _MAX_LEN:
        text = text[:_MAX_LEN].rstrip() + "…"
    return text or "I'm not sure how to answer that yet."
