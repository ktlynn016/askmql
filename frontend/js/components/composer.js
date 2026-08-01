ASKMQL.components.composer = (function () {
  function wire(textareaEl, sendBtnEl, onSend) {
    function autoGrow() {
      textareaEl.style.height = "auto";
      textareaEl.style.height = Math.min(textareaEl.scrollHeight, 120) + "px";
    }
    function trigger() {
      var text = textareaEl.value.trim();
      if (!text) return;
      textareaEl.value = "";
      autoGrow();
      onSend(text);
    }

    textareaEl.addEventListener("input", autoGrow);
    textareaEl.addEventListener("keydown", function (e) {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        trigger();
      }
    });
    sendBtnEl.addEventListener("click", trigger);

    return { send: trigger, setValue: function (v) { textareaEl.value = v; autoGrow(); } };
  }

  return { wire: wire };
})();
