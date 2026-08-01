/* Inline SVG icon sprite -- replaces an icon font/CDN so the app
   needs zero internet access. injectIconSprite() inserts the <symbol>
   defs once per page; icon(name) returns markup referencing one. */
ASKMQL.core.icons = (function () {
  var SPRITE = ""
    + '<svg style="position:absolute;width:0;height:0;overflow:hidden" aria-hidden="true"><defs>'
    + '<symbol id="icon-book-bookmark" viewBox="0 0 24 24"><path d="M5 3h11a2 2 0 0 1 2 2v16l-6-3-6 3V5a2 2 0 0 1 2-2z"/></symbol>'
    + '<symbol id="icon-comments" viewBox="0 0 24 24"><path d="M4 5h16a1 1 0 0 1 1 1v9a1 1 0 0 1-1 1H9l-5 4V6a1 1 0 0 1 1-1z"/><circle cx="9" cy="10.5" r="0.6" fill="currentColor" stroke="none"/><circle cx="12" cy="10.5" r="0.6" fill="currentColor" stroke="none"/><circle cx="15" cy="10.5" r="0.6" fill="currentColor" stroke="none"/></symbol>'
    + '<symbol id="icon-arrow-right" viewBox="0 0 24 24"><line x1="4" y1="12" x2="20" y2="12"/><polyline points="14 6 20 12 14 18"/></symbol>'
    + '<symbol id="icon-arrow-left" viewBox="0 0 24 24"><line x1="20" y1="12" x2="4" y2="12"/><polyline points="10 6 4 12 10 18"/></symbol>'
    + '<symbol id="icon-plus" viewBox="0 0 24 24"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></symbol>'
    + '<symbol id="icon-search" viewBox="0 0 24 24"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></symbol>'
    + '<symbol id="icon-bars" viewBox="0 0 24 24"><line x1="4" y1="7" x2="20" y2="7"/><line x1="4" y1="12" x2="20" y2="12"/><line x1="4" y1="17" x2="20" y2="17"/></symbol>'
    + '<symbol id="icon-trash" viewBox="0 0 24 24"><path d="M4 7h16"/><path d="M10 11v6"/><path d="M14 11v6"/><path d="M6 7l1 13a2 2 0 0 0 2 2h6a2 2 0 0 0 2-2l1-13"/><path d="M9 7V4a1 1 0 0 1 1-1h4a1 1 0 0 1 1 1v3"/></symbol>'
    + '<symbol id="icon-pen" viewBox="0 0 24 24"><path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4 12.5-12.5z"/></symbol>'
    + '<symbol id="icon-robot" viewBox="0 0 24 24"><rect x="5" y="8" width="14" height="10" rx="2"/><line x1="12" y1="4" x2="12" y2="8"/><circle cx="12" cy="4" r="1" fill="currentColor" stroke="none"/><circle cx="9" cy="13" r="1" fill="currentColor" stroke="none"/><circle cx="15" cy="13" r="1" fill="currentColor" stroke="none"/><line x1="9" y1="17" x2="15" y2="17"/></symbol>'
    + '<symbol id="icon-code" viewBox="0 0 24 24"><polyline points="8 6 3 12 8 18"/><polyline points="16 6 21 12 16 18"/></symbol>'
    + '<symbol id="icon-book" viewBox="0 0 24 24"><path d="M4 5a2 2 0 0 1 2-2h12v18H6a2 2 0 0 1-2-2V5z"/><line x1="8" y1="7" x2="14" y2="7"/><line x1="8" y1="11" x2="14" y2="11"/></symbol>'
    + '<symbol id="icon-database" viewBox="0 0 24 24"><ellipse cx="12" cy="6" rx="8" ry="3"/><path d="M4 6v12c0 1.66 3.58 3 8 3s8-1.34 8-3V6"/><path d="M4 12c0 1.66 3.58 3 8 3s8-1.34 8-3"/></symbol>'
    + '<symbol id="icon-network-wired" viewBox="0 0 24 24"><circle cx="6" cy="6" r="2"/><circle cx="18" cy="6" r="2"/><circle cx="12" cy="18" r="2"/><line x1="6" y1="8" x2="12" y2="16"/><line x1="18" y1="8" x2="12" y2="16"/><line x1="6" y1="6" x2="18" y2="6"/></symbol>'
    + '<symbol id="icon-bullhorn" viewBox="0 0 24 24"><path d="M3 10v4h3l6 4V6l-6 4H3z"/><path d="M14 9a4 4 0 0 1 0 6"/><path d="M17 7a7 7 0 0 1 0 10"/></symbol>'
    + '<symbol id="icon-microphone" viewBox="0 0 24 24"><rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5 11a7 7 0 0 0 14 0"/><line x1="12" y1="18" x2="12" y2="22"/><line x1="9" y1="22" x2="15" y2="22"/></symbol>'
    + '<symbol id="icon-send" viewBox="0 0 24 24"><polygon points="22 2 15 22 11 13 2 9 22 2"/></symbol>'
    + '<symbol id="icon-xmark" viewBox="0 0 24 24"><line x1="6" y1="6" x2="18" y2="18"/><line x1="6" y1="18" x2="18" y2="6"/></symbol>'
    + '<symbol id="icon-moon" viewBox="0 0 24 24"><path d="M21 12.5A9 9 0 1 1 11.5 3a7 7 0 0 0 9.5 9.5z"/></symbol>'
    + '<symbol id="icon-bell" viewBox="0 0 24 24"><path d="M6 9a6 6 0 0 1 12 0c0 4 1.5 5.5 1.5 5.5H4.5S6 13 6 9z"/><path d="M10 19a2 2 0 0 0 4 0"/></symbol>'
    + '<symbol id="icon-language" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><line x1="3" y1="12" x2="21" y2="12"/><path d="M12 3a14 14 0 0 1 0 18"/><path d="M12 3a14 14 0 0 0 0 18"/></symbol>'
    + '<symbol id="icon-chevron-right" viewBox="0 0 24 24"><polyline points="9 6 15 12 9 18"/></symbol>'
    + '<symbol id="icon-info" viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><line x1="12" y1="11" x2="12" y2="16"/><circle cx="12" cy="8" r="1" fill="currentColor" stroke="none"/></symbol>'
    + '<symbol id="icon-shield" viewBox="0 0 24 24"><path d="M12 3l7 3v6c0 5-3 8-7 9-4-1-7-4-7-9V6l7-3z"/><line x1="12" y1="3" x2="12" y2="21"/></symbol>'
    + '<symbol id="icon-logout" viewBox="0 0 24 24"><path d="M9 4H5a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h4"/><polyline points="15 16 20 11 15 6"/><line x1="20" y1="11" x2="8" y2="11"/></symbol>'
    + '<symbol id="icon-graduation-cap" viewBox="0 0 24 24"><path d="M12 3 2 8l10 5 10-5-10-5z"/><path d="M6 11v5c0 1.5 3 3 6 3s6-1.5 6-3v-5"/></symbol>'
    + '<symbol id="icon-user" viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/></symbol>'
    + '<symbol id="icon-brain" viewBox="0 0 24 24"><path d="M9 3a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5h1a3 3 0 0 0 2-1"/><path d="M15 3a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5h-1a3 3 0 0 1-2-1"/><line x1="12" y1="3" x2="12" y2="20"/></symbol>'
    + '<symbol id="icon-broom" viewBox="0 0 24 24"><line x1="19" y1="5" x2="10" y2="14"/><path d="M10 14c-2-1-5 0-5 2.5S7.5 19 9.5 18"/><line x1="16" y1="2" x2="21" y2="7"/></symbol>'
    + '<symbol id="icon-diagram" viewBox="0 0 24 24"><rect x="4" y="4" width="6" height="4" rx="1"/><rect x="14" y="4" width="6" height="4" rx="1"/><rect x="9" y="16" width="6" height="4" rx="1"/><line x1="7" y1="8" x2="7" y2="12"/><line x1="17" y1="8" x2="17" y2="12"/><line x1="7" y1="12" x2="17" y2="12"/><line x1="12" y1="12" x2="12" y2="16"/></symbol>'
    + '<symbol id="icon-chart-line" viewBox="0 0 24 24"><polyline points="4 19 4 5"/><polyline points="4 19 20 19"/><polyline points="7 15 11 10 14 13 19 6"/></symbol>'
    + '<symbol id="icon-server" viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="6" rx="1"/><rect x="3" y="14" width="18" height="6" rx="1"/><circle cx="7" cy="7" r="0.7" fill="currentColor" stroke="none"/><circle cx="7" cy="17" r="0.7" fill="currentColor" stroke="none"/></symbol>'
    + '<symbol id="icon-router" viewBox="0 0 24 24"><rect x="3" y="10" width="18" height="7" rx="1"/><line x1="7" y1="10" x2="7" y2="6"/><line x1="12" y1="10" x2="12" y2="4"/><circle cx="7" cy="13.5" r="1" fill="currentColor" stroke="none"/><circle cx="11" cy="13.5" r="1" fill="currentColor" stroke="none"/></symbol>'
    + '<symbol id="icon-thumbs-up" viewBox="0 0 24 24"><path d="M7 22V11l5-8 1.5 1L12 11h7a2 2 0 0 1 2 2.3l-1.4 7A2 2 0 0 1 17.6 22H7z"/><path d="M7 11H3v11h4"/></symbol>'
    + '<symbol id="icon-thumbs-down" viewBox="0 0 24 24"><path d="M17 2v11l-5 8-1.5-1L12 13H5a2 2 0 0 1-2-2.3l1.4-7A2 2 0 0 1 6.4 2H17z"/><path d="M17 13h4V2h-4"/></symbol>'
    + '</defs></svg>';

  var injected = false;

  function injectIconSprite() {
    if (injected) return;
    document.body.insertAdjacentHTML("afterbegin", SPRITE);
    injected = true;
  }

  function icon(name, extraAttrs) {
    var attrs = extraAttrs || "";
    return '<svg class="icon" ' + attrs + '><use href="#icon-' + name + '"></use></svg>';
  }

  return { injectIconSprite: injectIconSprite, icon: icon };
})();
