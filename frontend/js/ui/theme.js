/* Dark mode toggle backing the Profile screen's "Dark Mode" setting.
   No localStorage (see privacy note in js/state/store.js) -- theme
   resets to light on navigation/reload, same tradeoff as conversation
   history in this offline demo build. */
ASKMQL.ui.theme = (function () {
  function isDark() { return document.documentElement.classList.contains("theme-dark"); }
  function setDark(on) { document.documentElement.classList.toggle("theme-dark", !!on); }
  function toggle() { setDark(!isDark()); return isDark(); }
  return { isDark: isDark, setDark: setDark, toggle: toggle };
})();
