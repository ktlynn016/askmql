from core.config import Config
from adapters.vector.in_memory_adapter import InMemoryAdapter


def get_vector_store():
    # Add real backends (pgvector, Pinecone, Qdrant, ...) here as
    # VECTOR_STORE options grow.
    return InMemoryAdapter()
