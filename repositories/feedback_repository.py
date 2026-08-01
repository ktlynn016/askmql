from models.feedback import Feedback
from repositories.base import BaseRepository


class FeedbackRepository(BaseRepository):
    def create(self, message_id, rating, note=None):
        item = Feedback(message_id=message_id, rating=rating, note=note)
        self._add(item)
        self._commit()
        return item

    def list_for_message(self, message_id):
        return Feedback.query.filter_by(message_id=message_id).all()
