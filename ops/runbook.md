# Runbook

## First-time local setup
1. `docker compose -f ops/docker/docker-compose.yml up --build` (or
   run MySQL via XAMPP + `python backend/app.py` directly — see
   `backend/README.md`).
2. Load migrations + seeds (commands printed in
   `ops/docker/docker-compose.yml`'s header comment).
3. Open `frontend/index.html` directly in a browser (no server
   needed — it runs on local dummy data until wired to the API).

## Common issues

**"Can't connect to MySQL"**
Check `DB_HOST`/`DATABASE_URL` in `.env` matches where MySQL is
actually running (XAMPP = `localhost`, Docker Compose = `mysql`,
a managed host = whatever they gave you).

**Chat replies are always the generic fallback text**
Means `services/retrieval/lexical.py` found nothing. Check the seed
data loaded (`SELECT COUNT(*) FROM books;`) and that the query has a
4+ letter word matching a title/author, or a recognized category
keyword (see `_CATEGORY_KEYWORDS` in `lexical.py`).

**Admin endpoints return 401**
Log in as the librarian demo account first (`POST /api/v1/auth/login`
with `identifier: librarian@gsu-mosqueda.edu.ph`, see
`backend/seeds/users.sql`), then call `/admin/*` with the same
browser session (cookies included) or the same `fetch(..., {credentials:
"include"})` client. A student session gets 401 too — `/admin/*`
requires the `librarian` role specifically.

**Login works but the session doesn't stick across requests**
Almost always CORS: `CORS_ORIGINS` in `.env` must be the frontend's
exact origin (not `*`), and the frontend must send
`credentials: "include"` on every `fetch` call — see
`frontend/js/api/auth.js`. Also check `SESSION_COOKIE_SECURE` isn't
`1` while testing over plain HTTP (secure cookies are dropped by the
browser without HTTPS).

**Want to reset the database**
Drop and recreate: `DROP DATABASE askmql;` then re-run the migration
+ seed steps from scratch.

## Deploying a change
1. `pytest tests/` and `python -m eval.run_eval` locally first.
2. Push — CI (`ops/ci/github-actions.yml`) runs the same checks.
3. New DB changes go in a new `backend/migrations/000N_*.sql` file,
   never edit an already-applied one. Apply it manually on the
   deployed database (no auto-migrate step configured).
4. Deploy backend (Render/Railway/PythonAnywhere) and frontend
   (Vercel/Netlify) — they deploy independently.

## Rolling back
No automated rollback. Redeploy the previous backend build/commit;
for a bad migration, hand-write and apply a corrective SQL statement
(see "forward-only" note in `backend/migrations/README.md`).
