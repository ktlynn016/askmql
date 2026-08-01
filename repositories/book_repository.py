from models.book import Book
from models.category import Category
from repositories.base import BaseRepository


class BookRepository(BaseRepository):
    def get(self, book_id):
        return Book.query.get(book_id)

    def list(self, query=None, category=None, available_only=False):
        qs = Book.query
        if category:
            qs = qs.join(Category).filter(Category.name.ilike(category))
        if query:
            qs = qs.filter(Book.title.ilike(f"%{query}%"))
        if available_only:
            qs = qs.filter_by(is_available=True)
        return qs.order_by(Book.title.asc()).all()

    def all(self):
        return Book.query.all()

    def title_like(self, text):
        return Book.query.filter(Book.title.ilike(f"%{text}%")).all()

    def by_category_name(self, category_name):
        return Book.query.join(Category).filter(Category.name == category_name).all()

    def set_availability(self, book_id, is_available):
        book = self.get(book_id)
        if not book:
            return None
        book.is_available = is_available
        self._commit()
        return book
