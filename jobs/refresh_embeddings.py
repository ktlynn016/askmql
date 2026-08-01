"""Recomputes embeddings for every book and upserts them into the
configured vector store. Currently a no-op because the default
embeddings/vector adapters are stubs (see adapters/embeddings/none_adapter.py,
adapters/vector/in_memory_adapter.py) -- becomes real once a real
provider is configured via EMBEDDINGS_PROVIDER / VECTOR_STORE.
"""
from core.logging import get_logger
from core.config import Config
from adapters.embeddings.factory import get_embeddings_adapter
from adapters.vector.factory import get_vector_store
from repositories.book_repository import BookRepository

logger = get_logger("askmql.jobs.refresh_embeddings")


def run():
    if Config.EMBEDDINGS_PROVIDER == "none":
        logger.info("refresh_embeddings: EMBEDDINGS_PROVIDER=none, skipping")
        return {"updated": 0, "skipped": True}

    repo = BookRepository()
    embeddings = get_embeddings_adapter()
    store = get_vector_store()

    books = repo.all()
    texts = [f"{b.title} {b.description or ''}" for b in books]
    vectors = embeddings.embed(texts)
    store.upsert(
        ids=[b.id for b in books],
        vectors=vectors,
        metadata=[{"title": b.title} for b in books],
    )
    logger.info("refresh_embeddings: updated %d books", len(books))
    return {"updated": len(books), "skipped": False}


if __name__ == "__main__":
    print(run())
