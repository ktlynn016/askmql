"""Retrieval quality metrics for eval/run_eval.py."""


def hit_at_k(retrieved_ids, expected_ids, k=4):
    top_k = set(retrieved_ids[:k])
    return 1.0 if top_k & set(expected_ids) else 0.0


def recall_at_k(retrieved_ids, expected_ids, k=4):
    if not expected_ids:
        return None
    top_k = set(retrieved_ids[:k])
    hit = len(top_k & set(expected_ids))
    return hit / len(expected_ids)
