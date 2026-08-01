# Deploying ASKMQL: Vercel (frontend) + Render (backend) + Railway (MySQL)

This is the exact path for the setup you're using: frontend on Vercel,
backend on Render (not Vercel — Vercel's serverless functions don't
hold a persistent MySQL connection well), database staying MySQL on
Railway. Do these in order — each step needs the previous one's output.

## 1. Database first: Railway MySQL

1. Go to [railway.app](https://railway.app), sign in, **New Project → Provision MySQL**.
2. Once it's up, open the MySQL service → **Connect** tab → copy the
   **connection URL** (looks like `mysql://user:pass@host:port/railway`).
3. Open Railway's **Data** tab (or use a MySQL client / TablePlus /
   phpMyAdmin pointed at that connection) and run these files from
   `backend/`, **in this exact order**:
   - `migrations/0001_initial_schema.sql`
   - `migrations/0002_add_feedback_and_query_log.sql`
   - `migrations/0003_add_auth.sql`
   - `seeds/sample_catalog.sql`
   - `seeds/announcements.sql`
   - `seeds/users.sql`
4. Keep that connection URL handy for step 2.

## 2. Backend on Render

1. Push the `askmql` project to a GitHub repo (Render deploys from Git).
2. Go to [render.com](https://render.com) → **New → Web Service** → connect that repo.
3. **Root Directory**: `backend`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `gunicorn wsgi:app` (already set as the default via `backend/Procfile`)
6. Add these **Environment Variables** in Render's dashboard:
   ```
   DATABASE_URL=<the Railway MySQL URL from step 1, but change mysql:// to mysql+pymysql://>
   SECRET_KEY=<generate a random string>
   CORS_ORIGINS=<your Vercel URL, e.g. https://askmql.vercel.app -- can update this after step 3>
   SESSION_COOKIE_SAMESITE=None
   SESSION_COOKIE_SECURE=1
   FLASK_DEBUG=0
   ```
   `SESSION_COOKIE_SAMESITE=None` + `SESSION_COOKIE_SECURE=1` are
   required because the frontend (Vercel) and backend (Render) are on
   different domains — this is what makes login work cross-site.
7. Deploy. Render gives you a URL like `https://askmql-backend.onrender.com`.
8. Sanity check it's alive: open `https://askmql-backend.onrender.com/api/v1/health`
   in a browser — you should see `{"status": "ok", ...}`.

## 3. Frontend on Vercel

1. In `frontend/js/core/constants.js`, set:
   ```js
   USE_API: true,
   API_BASE_URL: "https://askmql-backend.onrender.com/api/v1",
   ```
   (use your actual Render URL from step 2, with `/api/v1` on the end)
2. Deploy `frontend/` to Vercel the same way as before (drag-and-drop
   at vercel.com/drop, or push and import the repo with Root Directory
   set to `frontend`).
3. Copy the URL Vercel gives you (e.g. `https://askmql.vercel.app`).

## 4. Close the loop

Go back to Render's environment variables (step 2.6) and make sure
`CORS_ORIGINS` is set to the **exact** Vercel URL from step 3 — no
trailing slash, exact scheme (`https://`) and domain. Save — Render
will redeploy automatically.

## 5. Test it for real

Open your Vercel URL, go through `login.html`, and sign in as the
seeded librarian (`librarian@gsu-mosqueda.edu.ph` / `librarian123`) or
student (`2023-0114` / `student123`). If login works and *stays*
logged in when you navigate to `history.html` or `profile.html`,
everything's wired correctly — that persistence is exactly what was
impossible in offline demo mode and is now working for real.

## Troubleshooting

**Login fails / CORS errors in the browser console**
`CORS_ORIGINS` on Render doesn't exactly match the Vercel URL. Check
for `http` vs `https`, trailing slashes, or a stale value.

**Login "works" but doesn't persist across pages**
`SESSION_COOKIE_SAMESITE` or `SESSION_COOKIE_SECURE` isn't set
correctly on Render (see step 2.6) — cross-site cookies need both.

**500 errors from the backend**
Check Render's logs (dashboard → your service → Logs). Usually a
`DATABASE_URL` typo, or a migration step from section 1.3 was skipped.

**Render free tier spins down when idle**
First request after inactivity can take 30–60 seconds to wake up —
that's normal on Render's free tier, not a bug.
