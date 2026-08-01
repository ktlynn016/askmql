# 0001: Layered backend architecture (routes → controllers → services → repositories)

## Status
Accepted

## Context
The original backend was a flat Flask app (routes → controllers →
services → models). That's fine for a handful of CRUD endpoints, but
ASKMQL's core feature is a chat pipeline that needs to grow into real
retrieval-augmented generation: query rewriting, lexical + semantic
search, fusion/reranking, prompt construction, and LLM calls. Bolting
all of that into one `chat_service.py` would make it hard to test,
swap providers, or reason about independently.

## Decision
Split `services/` into five sub-packages (`chat`, `retrieval`,
`generation`, `catalog`, `analytics`) and introduce a `repositories/`
layer between services and SQLAlchemy models, plus an `adapters/`
layer for anything that talks to an external system (LLM provider,
embeddings provider, vector store, catalog feed).

`services/chat/orchestrator.py` is the single entry point for a chat
turn; every stage it calls (rewrite, intent, retrieval, generation,
memory) is independently testable and independently swappable.

## Consequences
- More files, more indirection for simple CRUD (books, announcements) —
  accepted as the cost of making the chat pipeline growable.
- Adapters default to no-op/template implementations, so the app runs
  with zero API keys and zero external dependencies until someone
  opts into real LLM/embeddings/vector providers.
- `eval/run_eval.py` and `tests/` can target individual services
  without spinning up the whole app.
