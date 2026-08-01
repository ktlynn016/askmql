"""Runs services/retrieval against seeds/gold_set.json and reports
hit@k / recall@k. This is what you run after changing lexical.py,
semantic.py, fusion.py, or rerank.py to check you didn't regress
retrieval quality.

Usage (from backend/, with the app's Python env active and a seeded
database):
    python -m eval.run_eval
"""
import json
import os

from eval.metrics import hit_at_k, recall_at_k
from services.retrieval import fusion, rerank

_GOLD_SET_PATH = os.path.join(os.path.dirname(__file__), "..", "seeds", "gold_set.json")


def load_gold_set(path=_GOLD_SET_PATH):
    with open(path) as f:
        return json.load(f)["cases"]


def run(k=4):
    cases = load_gold_set()
    hits, recalls = [], []

    for case in cases:
        candidates = fusion.retrieve(case["query"])
        ranked = rerank.rerank(case["query"], candidates, top_k=k)
        retrieved_ids = [b.id for b in ranked]

        hits.append(hit_at_k(retrieved_ids, case["expected_book_ids"], k=k))
        r = recall_at_k(retrieved_ids, case["expected_book_ids"], k=k)
        if r is not None:
            recalls.append(r)

    report = {
        "cases": len(cases),
        f"hit@{k}": round(sum(hits) / len(hits), 3) if hits else None,
        f"recall@{k}": round(sum(recalls) / len(recalls), 3) if recalls else None,
    }
    return report


if __name__ == "__main__":
    print(run())
