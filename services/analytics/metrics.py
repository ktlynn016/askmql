"""Rolls query_logs up into simple aggregate metrics for the admin
dashboard (avg latency, top intents, zero-result rate). Deliberately
computed in Python rather than raw SQL for readability; fine at this
data volume -- move to SQL aggregates if query_logs gets large."""
from collections import Counter

from services.analytics.query_log import recent


def summary(limit=500):
    logs = recent(limit=limit)
    if not logs:
        return {"count": 0, "avg_latency_ms": 0, "zero_result_rate": 0, "top_intents": []}

    count = len(logs)
    avg_latency = sum(l.latency_ms or 0 for l in logs) / count
    zero_result = sum(1 for l in logs if (l.result_count or 0) == 0) / count
    top_intents = Counter(l.intent for l in logs if l.intent).most_common(5)

    return {
        "count": count,
        "avg_latency_ms": round(avg_latency, 1),
        "zero_result_rate": round(zero_result, 3),
        "top_intents": [{"intent": i, "count": c} for i, c in top_intents],
    }
