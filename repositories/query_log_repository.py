from models.query_log import QueryLog
from repositories.base import BaseRepository


class QueryLogRepository(BaseRepository):
    def create(self, query_text, conversation_id=None, intent=None, result_count=0, latency_ms=None):
        item = QueryLog(
            query_text=query_text,
            conversation_id=conversation_id,
            intent=intent,
            result_count=result_count,
            latency_ms=latency_ms,
        )
        self._add(item)
        self._commit()
        return item

    def recent(self, limit=100):
        return QueryLog.query.order_by(QueryLog.created_at.desc()).limit(limit).all()
