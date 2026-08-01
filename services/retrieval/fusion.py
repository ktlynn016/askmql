"""Merge lexical + semantic hits, de-duplicated, lexical-first (since
semantic is a no-op today -- see semantic.py). This is the single
seam chat/orchestrator.py calls; it doesn't know or care whether
semantic search is actually active."""
from services.retrieval import lexical, semantic


def retrieve(text: str, top_k: int = 4):
    lexical_hits = lexical.search(text)
    semantic_hits = semantic.search(text, top_k=top_k)

    seen = set()
    merged = []
    for book in lexical_hits + semantic_hits:
        if book.id not in seen:
            seen.add(book.id)
            merged.append(book)
    return merged
