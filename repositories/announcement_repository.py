from models.announcement import Announcement
from repositories.base import BaseRepository


class AnnouncementRepository(BaseRepository):
    def list(self):
        return Announcement.query.order_by(Announcement.posted_at.desc()).all()

    def create(self, message):
        item = Announcement(message=message)
        self._add(item)
        self._commit()
        return item
