from abc import ABC, abstractmethod


class CatalogFeedAdapter(ABC):
    """Interface for pulling book records from an external system of
    record (a real ILS/library catalog export, a spreadsheet feed,
    etc). jobs/sync_catalog.py depends on this, not on any concrete
    source -- so swapping the feed means adding one adapter here."""

    @abstractmethod
    def fetch_records(self) -> list:
        """Return a list of plain dicts describing books to upsert."""
        raise NotImplementedError
