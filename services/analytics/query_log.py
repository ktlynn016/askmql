from repositories.query_log_repository import QueryLogRepository

_repo = QueryLogRepository()


def record(query_text, conversation_id=None, intent=None, result_count=0, latency_ms=None):
    return _repo.create(
        query_text,
        conversation_id=conversation_id,
        intent=intent,
        result_count=result_count,
        latency_ms=latency_ms,
    )


def recent(limit=100):
    return _repo.recent(limit=limit)
