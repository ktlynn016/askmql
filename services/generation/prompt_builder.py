"""Builds the system/user prompt pair from retrieved books + the
user's message. Consumed by llm_client.py. Kept separate from the
LLM client so prompt changes don't require touching adapter code."""

_SYSTEM_PROMPT = (
    "You are ASKMQL, the AI library assistant for the Guimaras State "
    "University Mosqueda Campus Library. Answer in a friendly, "
    "professional tone using only the catalog context provided."
)


def build(user_text: str, books: list, announcements: list = None):
    if announcements:
        joined = " ".join(announcements)
        user_prompt = f"Here are today's library announcements: {joined}"
    elif books:
        titles = ", ".join(b.title for b in books[:4])
        user_prompt = f"Here's what I found in the catalog: {titles}."
    else:
        user_prompt = (
            "I couldn't find an exact match for that in the catalog yet. "
            "Try asking about AI, programming, databases, or networking "
            "books, or give me a title or author to search for."
        )
    return _SYSTEM_PROMPT, user_prompt
