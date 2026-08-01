/* Generic open/close helper for the details + profile overlays
   (both just toggle an "open" class -- see css/components/modals.css). */
ASKMQL.ui.modal = (function () {
  function open(el) { el.classList.add("open"); }
  function close(el) { el.classList.remove("open"); }
  return { open: open, close: close };
})();
