"""Pulls records from the configured catalog feed adapter and upserts
them into MySQL. Run manually (python -m jobs.sync_catalog), on a
schedule (cron/Task Scheduler), or via POST /api/v1/admin/sync-catalog.

Today's default adapter (MySQLCatalogAdapter) just reads back what's
already in the DB, so this is a no-op until a real external feed
adapter is added under adapters/catalog/.
"""
from core.logging import get_logger
from adapters.catalog.mysql_catalog_adapter import MySQLCatalogAdapter

logger = get_logger("askmql.jobs.sync_catalog")


def run():
    adapter = MySQLCatalogAdapter()
    records = adapter.fetch_records()
    logger.info("sync_catalog: fetched %d records (no-op with default adapter)", len(records))
    return {"synced": len(records)}


if __name__ == "__main__":
    print(run())
