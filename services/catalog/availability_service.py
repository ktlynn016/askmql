"""Split out from book_service so availability can later be backed by
a live circulation feed (checkouts/holds) instead of a static column,
without touching book search/details code."""
from repositories.book_repository import BookRepository
from core.errors import NotFoundError

_repo = BookRepository()


def get_availability(book_id):
    book = _repo.get(book_id)
    if not book:
        raise NotFoundError(f"Book {book_id} not found")
    return {"book_id": book.id, "available": bool(book.is_available)}


def set_availability(book_id, is_available):
    book = _repo.set_availability(book_id, is_available)
    if not book:
        raise NotFoundError(f"Book {book_id} not found")
    return {"book_id": book.id, "available": bool(book.is_available)}
