"""Simple in-process vector store for local dev/demo. Not persisted,
not clustered -- swap for a real vector DB (pgvector, Pinecone, etc.)
by adding an adapter here and updating VECTOR_STORE in config."""
from adapters.vector.base import VectorStoreAdapter


class InMemoryAdapter(VectorStoreAdapter):
    def __init__(self):
        self._store = {}  # id -> (vector, metadata)

    def upsert(self, ids, vectors, metadata):
        for _id, vec, meta in zip(ids, vectors, metadata):
            self._store[_id] = (vec, meta)

    def query(self, vector, top_k: int):
        # No real embeddings configured by default (see
        # adapters/embeddings/none_adapter.py) so there is nothing
        # meaningful to score against yet -- returns empty.
        if not vector or not self._store:
            return []
        return []
