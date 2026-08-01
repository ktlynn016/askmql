"""Tiny shared helper so repositories don't each re-import db.session."""
from database.db import db


class BaseRepository:
    def _commit(self):
        db.session.commit()

    def _add(self, entity):
        db.session.add(entity)
        return entity
