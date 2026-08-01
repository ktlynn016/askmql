# ASKMQL Frontend

Static, multi-page, framework-free (HTML5 + CSS3 + vanilla ES5 JS) —
runs by opening `index.html` directly from disk. No build step, no
server, no internet connection required.

## Pages

| File | Purpose |
|---|---|
| `index.html` | Splash + welcome screens → `login.html` |
| `login.html` | Student/librarian sign in, student sign-up, "continue as guest" |
| `chat.html` | Main chat screen (sidebar, composer, book cards, book details modal, sign out) |
| `book.html?id=N` | Standalone book detail page |
| `history.html` | Full conversation history list |
| `profile.html` | Profile + settings (dark mode toggle, working sign out) |
| `admin/index.html` | Librarian-only metrics dashboard — sign-in gate, then talks to the real backend |

## Login / signup / sign out

`js/api/auth.js` is dual-mode like everything else in `js/api/`:

- **Real backend** (`USE_API = true`): every call goes through
  `js/api/client.js`, which always sends `credentials: "include"` so
  the browser's own session cookie (set by the Flask backend — see
  `../backend/README.md`'s Authentication section) is sent/received
  automatically. This is a real, persistent, cross-page login, and
  it's **not** a JS storage API, so it doesn't conflict with the
  no-localStorage rule below.
- **Offline demo** (`USE_API = false`, the default): `js/state/demo-users.js`
  holds two hardcoded demo accounts (student `2023-0114` / `student123`,
  librarian `librarian@gsu-mosqueda.edu.ph` / `librarian123`) and
  checks plaintext passwords client-side — **this is a demo mechanism
  only**, not how real auth works; the actual backend always hashes
  passwords server-side.

`js/ui/auth-guard.js` is the shared "am I logged in" check used by
`chat.html`, `history.html`, and `profile.html`. In real API mode it
redirects to `login.html` when there's no session; in offline mode it
never redirects (see the no-localStorage note below for why) — pages
just render a "Guest" fallback instead.

## Why classic scripts, not ES modules

Every file under `js/` attaches to a shared `window.ASKMQL` namespace
instead of using `import`/`export`. That's deliberate: `type="module"`
scripts are blocked by CORS when a page is opened directly from disk
(`file://`) in Chrome and other browsers, which would break the
"just double-click index.html" requirement. Classic `<script src>`
tags have no such restriction.

## Folder structure

```
js/
├── core/        constants, DOM helpers, the inline SVG icon sprite
├── api/         client.js (real backend) + one file per resource,
│                each with a dummy-data fallback (see below)
├── state/       catalog-data.js (dummy catalog), store.js (in-memory
│                conversation state — no localStorage, see below)
├── ui/          toast, modal open/close, dark mode toggle
└── components/  book-card, message, sidebar, composer render functions

css/
├── tokens/      colors, typography, spacing — the design system values
├── base/        reset + global element defaults
├── components/  one file per UI component (buttons, cards, chat, sidebar, …)
├── layouts/     page-level layout (app shell vs. standalone page)
└── themes/      light (default) + dark (toggled from profile.html)

assets/
├── css/, js/    reserved for future vendor/bundled assets if a build
│                step is ever introduced — empty for now, source lives
│                in css/ and js/ above
└── img/, fonts/ reserved for real images/webfonts once the catalog
                  has real cover art (currently book covers are just
                  color + icon, no image files needed)
```

## Offline dummy data vs. the real backend

`js/core/constants.js` has one flag:

```js
ASKMQL.core.constants.USE_API = false;   // true = call the real backend
ASKMQL.core.constants.API_BASE_URL = "http://localhost:5000/api/v1";
```

Every file under `js/api/` checks this flag and either calls the real
backend (`js/api/client.js`) or falls back to local logic against
`js/state/catalog-data.js` — which mirrors `backend/seeds/sample_catalog.sql`
exactly, so results match either way. Flip it to `true` once the
backend from `../backend/` is running (see its README) to get real
persistence, real retrieval, and eventually real generation.

## No localStorage

Per the project's constraints, this app never uses
`localStorage`/`sessionStorage`. Conversation history, the dark mode
setting, and (in offline demo mode) the login session are all kept in
plain JS memory (`js/state/store.js`, `js/ui/theme.js`), which means
they **reset on every page navigation** (chat.html → history.html →
back, etc.) or reload. This is the honest tradeoff of "fully offline,
zero storage APIs" — wiring `USE_API = true` removes it entirely for
both: conversations live server-side in MySQL, and login lives in a
real browser session cookie (set by the server, never touched by this
app's JS — see the Login section above), both of which genuinely
persist across page loads.

## Accessibility

Semantic HTML landmarks (`header`, `main`, `aside`), keyboard-focusable
controls with visible focus rings (`css/base/reset.css`), and
`prefers-reduced-motion` support are baked in throughout.
