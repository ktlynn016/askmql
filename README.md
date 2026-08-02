# ASKMQL Backend

Flask + MySQL API for the ASKMQL library chatbot, structured as a
RAG-ready layered architecture:

```
routes/v1/  -->  controllers/  -->  services/  -->  repositories/  -->  models/
                                        |
                                    adapters/  (llm, embeddings, vector, catalog feed)
```

- **routes/v1/** — URL → controller wiring (Blueprints), versioned so `v2` can
  exist alongside it later without breaking anyone.
- **controllers/** — request/response glue only (parse JSON, call a service,
  serialize the result). No business logic lives here.
- **services/** — the actual logic, split by concern:
  - `chat/` — `orchestrator.py` is the entry point for `POST /chat`; it wires
    together `rewrite → intent → retrieval → generation → memory` and logs
    the turn. Read this file first.
  - `retrieval/` — `lexical.py` (today's real search, keyword/category
    matching against MySQL), `semantic.py` (embedding search — inert until
    an embeddings provider is configured), `fusion.py` (merges both),
    `rerank.py`, `filters.py`.
  - `generation/` — `prompt_builder.py`, `llm_client.py`, `validator.py`.
    `llm_client.py` calls whatever's configured in `adapters/llm/` — by
    default a template adapter with **no external API calls**.
  - `catalog/` — book + availability logic.
  - `analytics/` — query logging, feedback, metrics for the admin dashboard.
- **repositories/** — the only layer that talks to SQLAlchemy models directly.
- **adapters/** — interfaces + swappable implementations for `llm/`,
  `embeddings/`, `vector/`, and `catalog/` (an external ILS feed, eventually).
  Every adapter has a safe, dependency-free default so the app runs today
  with zero API keys; flipping a provider is a one-line config change plus
  filling in the corresponding adapter file.
- **jobs/** — `sync_catalog.py`, `refresh_embeddings.py`. Run manually,
  on a schedule, or via `POST /api/v1/admin/sync-catalog`.
- **migrations/** — versioned, forward-only SQL (`0001_*.sql`, `0002_*.sql`, …).
- **seeds/** — sample catalog/announcements data, plus `gold_set.json` for eval.
- **eval/** — `run_eval.py` scores the retrieval pipeline against `gold_set.json`
  (hit@k / recall@k). Run this after touching anything in `services/retrieval/`.
- **tests/** — `unit/` (no DB needed), `integration/` (needs a seeded DB),
  `e2e/` (full chat flow).

## Local setup (XAMPP)

1. Start Apache + MySQL in the XAMPP control panel.
2. Import, in order, via phpMyAdmin:
   - `migrations/0001_initial_schema.sql`
   - `migrations/0002_add_feedback_and_query_log.sql`
   - `migrations/0003_add_auth.sql`
   - `seeds/sample_catalog.sql`
   - `seeds/announcements.sql`
   - `seeds/users.sql` (demo student + librarian accounts)
3. ```
   python -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   cp .env.example .env
   ```
4. Run it:
   ```
   python app.py
   ```
   API is now at `http://localhost:5000/api/v1`.

No XAMPP? Set `AUTO_CREATE_TABLES=1` in `.env` for the first run only
(creates empty tables from the models), then seed data yourself.

## API endpoints (all under `/api/v1`)

| Method | Path                                | Description                                   |
|--------|--------------------------------------|-------------------------------------------------|
| GET    | `/health`                            | Health check                                    |
| POST   | `/auth/signup`                       | Register a student account (auto-logs-in)       |
| POST   | `/auth/login`                        | `{ identifier, password, role? }` — student_id or librarian email |
| POST   | `/auth/logout`                       | Clear the session                               |
| GET    | `/auth/me`                           | Current logged-in user (or `{user: null}`)      |
| POST   | `/chat`                              | `{ message, conversation_id? }` → full pipeline |
| GET    | `/books?q=&category=`                | List/search books                               |
| GET    | `/books/<id>`                        | Single book with related books                  |
| GET    | `/books/<id>/availability`           | Availability only                               |
| PUT    | `/books/<id>/availability`           | Update availability (`{ available: bool }`)     |
| GET    | `/recommendations?category=`         | A few available picks                           |
| GET    | `/announcements`                     | Current announcements                           |
| GET    | `/conversations`                     | List chat history                               |
| POST   | `/conversations`                     | Create a new conversation                       |
| PATCH  | `/conversations/<id>`                | Rename                                          |
| DELETE | `/conversations/<id>`                | Delete                                          |
| GET    | `/conversations/<id>/messages`       | Messages in a conversation                      |
| POST   | `/feedback`                          | `{ message_id, rating: up/down, note? }`        |
| GET    | `/admin/metrics`                     | Aggregate query metrics — requires librarian session |
| POST   | `/admin/sync-catalog`                | Trigger catalog sync — requires librarian session |

Full request/response schemas: `docs/api/openapi.yaml`.

## Authentication

`services/auth/auth_service.py` handles login/signup/logout;
`core/security.py` has the `login_required`/`require_role` decorators
routes use to gate access. Session state lives entirely in Flask's
signed, httpOnly session cookie — **never** in any client-side JS
storage, which is why the frontend never touches `localStorage`/
`sessionStorage` either (see `frontend/README.md`).

- **Students** self-register via `POST /auth/signup` (name, student ID,
  department, password) and are logged in immediately.
- **Librarians** don't self-register — seed or hand-create their
  accounts (see `seeds/users.sql`); they log in the same
  `POST /auth/login` endpoint with their email instead of a student ID.
- `/admin/*` requires a librarian session (`require_role("librarian")`).
- Demo accounts (seeded by `seeds/users.sql`): student `2023-0114` /
  `student123`, librarian `librarian@gsu-mosqueda.edu.ph` /
  `librarian123`. **Change or remove these before any real deployment.**

Because this relies on a real browser cookie (not JS-managed storage),
`CORS_ORIGINS` must be the frontend's exact origin — cookies aren't
sent to a wildcard `*` origin — and frontend requests must use
`fetch(..., { credentials: "include" })`, which `frontend/js/api/auth.js`
already does.

## Turning on real RAG

Three independent switches in `.env`, each with a corresponding adapter
to fill in:

1. `LLM_PROVIDER=anthropic` → implement `adapters/llm/anthropic_adapter.py`
2. `EMBEDDINGS_PROVIDER=<provider>` → add an adapter under `adapters/embeddings/`
3. `VECTOR_STORE=<store>` → add an adapter under `adapters/vector/`

Nothing in `routes/`, `controllers/`, or `services/chat/orchestrator.py`
needs to change — that's the point of the adapter seam.

## Tests

```
pip install -r requirements.txt
pytest tests/unit                 # no DB needed
pytest tests/integration tests/e2e  # needs a seeded database + .env
```

## Connecting the frontend

See `frontend/js/api/` — `client.js` reads `API_BASE_URL` (defaults to
`http://localhost:5000/api/v1`). The frontend still ships with local
dummy data by default so it works with zero backend running; point
`state/app-state.js` at the real API to switch over.

## Deployment

- **Backend**: Render, Railway, or PythonAnywhere. Set `.env` values as
  real environment variables; run with `gunicorn wsgi:app` (a
  `Procfile` is already set up for this).
- **Database**: Railway MySQL, Aiven MySQL, or Hostinger MySQL — run the
  migrations and seeds the same way as locally.
- **CORS**: set `CORS_ORIGINS` to the deployed frontend's exact URL —
  required for the login session cookie to work cross-origin.

For the exact combination of Vercel (frontend) + Render (backend) +
Railway (MySQL), see `ops/vercel-render-deploy-guide.md` — a full
step-by-step walkthrough.

See `ops/` for Dockerfiles, a docker-compose stack, and a CI workflow.
