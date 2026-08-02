/* Global namespace + shared constants.
   Loaded as a classic (non-module) script on purpose: ES modules
   (type="module") are blocked by CORS when a page is opened directly
   from disk (file://) in Chrome and some other browsers. Classic
   <script src="..."> tags have no such restriction, so every file in
   js/ attaches to window.ASKMQL instead of using import/export. This
   is what lets the whole app run with no server and no internet. */
window.ASKMQL = window.ASKMQL || {};
ASKMQL.core = ASKMQL.core || {};

ASKMQL.core.constants = {
  // ============================================================
  // GOING LIVE WITH THE REAL BACKEND (Render/Railway + MySQL)
  // ============================================================
  // 1. Deploy backend/ to Render or Railway (see backend/README.md
  //    and ops/vercel-render-deploy-guide.md) with a real MySQL
  //    database (Railway MySQL or Aiven MySQL).
  // 2. Copy the URL Render/Railway gives your backend, e.g.
  //    "https://askmql-backend.onrender.com/api/v1", and paste it
  //    into API_BASE_URL below.
  // 3. Flip USE_API to true.
  // 4. On the backend, set CORS_ORIGINS to this Vercel frontend's
  //    exact URL (e.g. "https://askmql.vercel.app") -- required for
  //    login to work, since cookies aren't sent to a wildcard origin.
  // 5. Redeploy this frontend to Vercel (drag the frontend folder in
  //    again, or push to the connected Git repo).
  //
  // Until you've done this, leave USE_API false -- the app runs
  // fully offline on built-in sample data either way, so nothing
  // breaks by deploying early.
   USE_API: true,
   API_BASE_URL: "https://askmql-backend.onrender.com/api/v1",
};
