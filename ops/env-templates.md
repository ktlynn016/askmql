# Environment templates by deploy target

## Local (XAMPP)
Use `backend/.env.example` as-is — defaults already match XAMPP's
default MySQL (root, no password, port 3306).

## Render / Railway (backend)
Set as service environment variables (not a committed .env file):
```
DATABASE_URL=mysql+pymysql://<user>:<password>@<host>:<port>/<db>
CORS_ORIGINS=https://<your-frontend-domain>
FLASK_DEBUG=0
SECRET_KEY=<generate a real secret -- this signs the session cookie>
SESSION_COOKIE_SAMESITE=None
SESSION_COOKIE_SECURE=1
```
`SESSION_COOKIE_SAMESITE=None` + `SESSION_COOKIE_SECURE=1` (HTTPS
required) is needed because the frontend and backend are on different
domains here. Change the demo passwords in `seeds/users.sql` (or
delete those rows and sign up real accounts) before going live.

## Railway MySQL / Aiven MySQL / Hostinger MySQL
Copy the connection string they give you directly into `DATABASE_URL`
above. Aiven typically requires SSL — if so add `?ssl_mode=REQUIRED`
(or the provider's documented equivalent) to the URL.

## Vercel / Netlify (frontend)
No env vars needed for the static files themselves. Update
`frontend/js/api/client.js`'s `API_BASE_URL` constant to point at the
deployed backend URL before deploying (or wire it to read from a
build-time env var if the hosting setup supports one).
