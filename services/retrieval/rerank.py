"""Placeholder reranking stage. Today just truncates to top_k in the
order fusion.py already produced (lexical relevance). Swap in a real
cross-encoder or LLM-based reranker here without touching callers."""


def rerank(query: str, books: list, top_k: int = 4):
    return books[:top_k]
