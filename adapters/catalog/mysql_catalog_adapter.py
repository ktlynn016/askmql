"""Default catalog feed: the MySQL database itself is the source of
truth (managed via database/schema.sql + database/seed.sql, or the
admin endpoints). This adapter exists so jobs/sync_catalog.py has a
consistent interface even before a real external ILS feed exists."""
from adapters.catalog.base import CatalogFeedAdapter
from repositories.book_repository import BookRepository


class MySQLCatalogAdapter(CatalogFeedAdapter):
    def __init__(self):
        self.repo = BookRepository()

    def fetch_records(self) -> list:
        return [b.to_dict() for b in self.repo.all()]
