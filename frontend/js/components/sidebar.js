ASKMQL.components.sidebar = (function () {
  var icon = ASKMQL.core.icons.icon;
  var esc = ASKMQL.core.dom.escapeHtml;

  /* Renders the conversation list into `container`. `onSelect`,
     `onRename`, `onDelete` are callbacks(conversationId). Used by both
     chat.html (sidebar) and history.html (full page). */
  function renderHistory(container, conversations, activeId, handlers) {
    handlers = handlers || {};
    container.innerHTML = "";
    conversations.forEach(function (c) {
      var el = document.createElement("div");
      el.className = "history-item" + (c.id === activeId ? " active" : "");
      el.innerHTML = ''
        + '<span class="htitle">' + esc(c.title) + '</span>'
        + '<span class="history-actions">'
        + icon("pen")
        + icon("trash")
        + '</span>';

      var icons = el.querySelectorAll(".history-actions .icon");
      icons[0].addEventListener("click", function (e) {
        e.stopPropagation();
        if (handlers.onRename) handlers.onRename(c.id, c.title);
      });
      icons[1].addEventListener("click", function (e) {
        e.stopPropagation();
        if (handlers.onDelete) handlers.onDelete(c.id);
      });
      el.addEventListener("click", function () {
        if (handlers.onSelect) handlers.onSelect(c.id);
      });

      container.appendChild(el);
    });
  }

  return { renderHistory: renderHistory };
})();
