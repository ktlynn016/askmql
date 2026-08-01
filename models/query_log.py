"""One row per chat turn: what was asked, which retrieval path/intent
handled it, how many results came back, and how long it took. Feeds
services/analytics/metrics.py and eval/run_eval.py."""
from datetime import datetime

from database.db import db


class QueryLog(db.Model):
    __tablename__ = "query_logs"

    id = db.Column(db.Integer, primary_key=True)
    conversation_id = db.Column(db.Integer, db.ForeignKey("conversations.id"), nullable=True)
    query_text = db.Column(db.Text, nullable=False)
    intent = db.Column(db.String(50))
    result_count = db.Column(db.Integer, default=0)
    latency_ms = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "conversation_id": self.conversation_id,
            "query_text": self.query_text,
            "intent": self.intent,
            "result_count": self.result_count,
            "latency_ms": self.latency_ms,
            "created_at": self.created_at.isoformat(),
        }
