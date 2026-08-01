"""No-op embeddings adapter -- the default. Returns empty vectors so
services/retrieval/semantic.py can detect "not configured" and skip
straight to lexical-only search, rather than crashing."""
from adapters.embeddings.base import EmbeddingsAdapter


class NoneAdapter(EmbeddingsAdapter):
    def embed(self, texts: list) -> list:
        return [[] for _ in texts]
