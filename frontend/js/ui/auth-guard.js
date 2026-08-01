/* Shared "am I logged in" check used by chat.html, history.html,
   profile.html. In real API mode this reflects a genuine, persistent
   browser session cookie and will redirect to login.html when there
   isn't one. In offline demo mode there's no persistence across page
   loads at all (see js/state/store.js), so this deliberately does
   NOT redirect -- it just resolves with whatever this page's
   in-memory session happens to be (often null), and callers render a
   "Guest" fallback instead of hard-blocking navigation. */
ASKMQL.ui.authGuard = (function () {
  function requireSession(options) {
    options = options || {};
    return ASKMQL.api.auth.me().then(function (user) {
      if (!user && ASKMQL.core.constants.USE_API) {
        window.location.href = options.loginPath || "login.html";
        return null;
      }
      return user;
    });
  }

  return { requireSession: requireSession };
})();
