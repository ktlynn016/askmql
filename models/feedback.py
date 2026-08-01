"""Thumbs up/down (or free-text note) on a single AI message.
Backs services/analytics/feedback.py and the eval loop (eval/run_eval.py
can pull low-rated real conversations into the gold set over time)."""
from datetime import datetime

from database.db import db


class Feedback(db.Model):
    __tablename__ = "feedback"

    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.Integer, db.ForeignKey("messages.id"), nullable=False)
    rating = db.Column(db.Enum("up", "down", name="feedback_rating"), nullable=False)
    note = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "message_id": self.message_id,
            "rating": self.rating,
            "note": self.note,
            "created_at": self.created_at.isoformat(),
        }
