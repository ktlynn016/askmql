# Evaluation

`backend/eval/run_eval.py` scores the retrieval pipeline
(`services/retrieval/`) against a small hand-written gold set
(`backend/seeds/gold_set.json`): a list of `{query, expected_book_ids}`
cases.

## Running it

```
cd backend
python -m eval.run_eval
```

Output looks like:

```json
{"cases": 7, "hit@4": 1.0, "recall@4": 0.86}
```

- **hit@k** — fraction of queries where at least one expected book
  appeared in the top k results. The headline number for "did the
  chatbot find something useful."
- **recall@k** — average fraction of each query's expected books that
  showed up in the top k. Useful for multi-book queries (e.g.
  "recommend programming books" expects several titles).

## What this measures today vs. later

Right now `services/retrieval/lexical.py` is the only active search
path — `semantic.py` is a documented no-op until an embeddings
provider is configured (see `docs/adr/0002-retrieval-adapter-seam.md`).
So today's eval numbers are purely a lexical-search score. Once real
embeddings + a vector store are wired in, re-run `run_eval.py` before
and after to confirm semantic search is actually additive rather than
just changing the numbers.

## Growing the gold set

`backend/seeds/gold_set.json` is intentionally small and hand-written.
As real usage happens, `services/analytics/query_log.py` records every
chat turn (query text, intent, result count, latency) — periodically
review low-`result_count` or thumbs-down (`services/analytics/feedback.py`)
queries from `query_logs`/`feedback` and add the ones that should have
worked into the gold set.

## Response quality (not yet automated)

`run_eval.py` only scores retrieval, not the generated reply text —
today's `generation/llm_client.py` uses a deterministic template
adapter, so there's nothing model-generated to grade yet. Once
`LLM_PROVIDER=anthropic` (or similar) is active, extend this
directory with a rubric-based or LLM-graded response quality check
before relying on eval numbers alone to judge chat quality.
