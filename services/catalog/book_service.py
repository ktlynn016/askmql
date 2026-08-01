from repositories.book_repository import BookRepository
from core.errors import NotFoundError

_repo = BookRepository()


def list_books(query=None, category=None):
    return _repo.list(query=query, category=category)


def get_book(book_id):
    book = _repo.get(book_id)
    if not book:
        raise NotFoundError(f"Book {book_id} not found")
    return book


def recommend(category=None, limit=4):
    books = _repo.list(category=category, available_only=True)
    return books[:limit]
