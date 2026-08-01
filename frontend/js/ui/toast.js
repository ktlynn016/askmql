ASKMQL.ui = ASKMQL.ui || {};

ASKMQL.ui.toast = (function () {
  var container = null;

  function ensureContainer() {
    if (container) return container;
    container = document.createElement("div");
    container.style.cssText = "position:fixed;bottom:20px;left:50%;transform:translateX(-50%);z-index:100;display:flex;flex-direction:column;gap:8px;align-items:center;";
    document.body.appendChild(container);
    return container;
  }

  function show(message) {
    var el = document.createElement("div");
    el.textContent = message;
    el.style.cssText = "background:var(--ink);color:#fff;padding:9px 16px;border-radius:999px;font-size:12.5px;font-family:var(--font-body);box-shadow:var(--shadow);opacity:0;transition:opacity .2s ease;";
    ensureContainer().appendChild(el);
    requestAnimationFrame(function () { el.style.opacity = "1"; });
    setTimeout(function () {
      el.style.opacity = "0";
      setTimeout(function () { el.remove(); }, 200);
    }, 1800);
  }

  return { show: show };
})();
