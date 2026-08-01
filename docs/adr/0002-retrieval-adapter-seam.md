# 0002: Adapter seam for LLM / embeddings / vector store / catalog feed

## Status
Accepted

## Context
The spec asks for "architecture that can later integrate with a RAG
backend using the GSU Mosqueda Campus Library catalog," but doesn't
specify which LLM, embeddings model, or vector database will
eventually be used — and none of those are available/needed for the
current placeholder-endpoint milestone.

## Decision
Define an abstract interface for each external dependency
(`adapters/llm/base.py`, `adapters/embeddings/base.py`,
`adapters/vector/base.py`, `adapters/catalog/base.py`) with a safe
default implementation that requires no API key or network call:
- `TemplateAdapter` (LLM) — returns the already-built plain-text reply.
- `NoneAdapter` (embeddings) — returns empty vectors.
- `InMemoryAdapter` (vector store) — no-op store.
- `MySQLCatalogAdapter` (catalog feed) — reads back from the app's own DB.

`core/config.py` selects the active adapter via env vars
(`LLM_PROVIDER`, `EMBEDDINGS_PROVIDER`, `VECTOR_STORE`).
`services/retrieval/semantic.py` checks for an empty embedding and
falls back to lexical-only search rather than erroring.

## Consequences
- Real providers can be added by writing one new adapter file each
  and flipping a config value — `services/`, `routes/`, and
  `controllers/` never change.
- Until real providers are configured, "semantic search" and "LLM
  generation" are honest no-ops rather than mocked-to-look-real
  behavior — `docs/evaluation/README.md` explains how to tell the
  difference when reading eval output.
