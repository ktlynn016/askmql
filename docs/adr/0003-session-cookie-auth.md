# 0003: Session-cookie auth (student + librarian), not JWT or localStorage

## Status
Accepted

## Context
The app needs a real login for two distinct account types (students,
who self-register; librarians, who don't) and a sign-out. The
frontend has a hard constraint of never using `localStorage`,
`sessionStorage`, or any client-side JS storage API. A token-based
scheme (JWT kept in JS memory or a JS-managed store) would either
violate that constraint or fail to persist across the frontend's
separate HTML pages (`chat.html`, `history.html`, `profile.html`, …),
since each page load is a fresh document with fresh JS state.

## Decision
Use Flask's built-in signed, httpOnly session cookie
(`flask.session`, backed by `SECRET_KEY`) as the only place login
state is stored. `services/auth/auth_service.py` sets `session["user_id"]`
and `session["role"]` on login/signup and clears it on logout;
`core/security.py`'s `login_required`/`require_role` decorators read
it. The frontend never reads or writes the cookie directly — the
browser attaches it automatically to every `fetch(..., {credentials:
"include"})` call in `frontend/js/api/auth.js` — so no JS storage API
is ever touched, and the login persists correctly across the
frontend's separate pages for real, for anyone running the actual
backend.

Both account types share one `users` table, split by a `role` enum
(`student`/`librarian`) and by which identifier they log in with
(`student_id` vs `email`).

## Consequences
- Requires the frontend to be served over HTTP(S) (any static server)
  rather than opened via `file://` for login to actually persist —
  cookies aren't reliably sent from a `file://` (`null`) origin. This
  doesn't affect the app's offline dummy-data mode, which still needs
  no server at all; it only applies once `USE_API` is turned on.
- `CORS_ORIGINS` must be a concrete origin, not `*`, since browsers
  won't send credentialed requests to a wildcard origin.
- No JWT library, no refresh-token complexity — appropriate for this
  app's scale. Revisit if the API needs to be called from a native
  mobile client someday, where cookie jars behave differently.
