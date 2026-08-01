"""Query rewriting placeholder -- e.g. resolving "it"/"that book" from
conversation history into an explicit title, or expanding abbreviations
("db" -> "database"). Currently a passthrough; orchestrator.py already
calls this so a real rewriter can be dropped in without touching it."""


def rewrite(text: str, conversation_history: list = None) -> str:
    return text
