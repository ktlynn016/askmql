"""Embedding-based retrieval -- inert until an embeddings provider and
vector store are configured (see adapters/embeddings, adapters/vector).
Returns [] rather than raising, so fusion.py can always call this
safely and lexical results carry the response either way."""
from adapters.embeddings.factory import get_embeddings_adapter
from adapters.vector.factory import get_vector_store
from repositories.book_repository import BookRepository

_embeddings = get_embeddings_adapter()
_vector_store = get_vector_store()
_repo = BookRepository()


def search(text: str, top_k: int = 4):
    vectors = _embeddings.embed([text])
    if not vectors or not vectors[0]:
        return []  # no embeddings provider configured

    hits = _vector_store.query(vectors[0], top_k=top_k)
    if not hits:
        return []

    ids = [book_id for book_id, _score in hits]
    books_by_id = {b.id: b for b in _repo.all() if b.id in ids}
    return [books_by_id[i] for i in ids if i in books_by_id]
