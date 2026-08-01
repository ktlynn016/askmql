ASKMQL.components.message = (function () {
  var icon = ASKMQL.core.icons.icon;
  var dom = ASKMQL.core.dom;

  function render(container, role, html) {
    var row = document.createElement("div");
    row.className = "msg-row " + role;
    var time = dom.formatTime(new Date());
    var avatarIcon = role === "ai" ? icon("book-bookmark") : icon("user");

    var feedback = "";
    if (role === "ai") {
      var mid = "m" + Date.now() + Math.floor(Math.random() * 1000);
      feedback = ''
        + '<div class="msg-feedback" data-message-id="' + mid + '">'
        + '  <button type="button" data-rating="up" title="Good answer">' + icon("thumbs-up") + '</button>'
        + '  <button type="button" data-rating="down" title="Not helpful">' + icon("thumbs-down") + '</button>'
        + '</div>';
    }

    row.innerHTML = ''
      + '<div class="msg-avatar ' + role + '">' + avatarIcon + '</div>'
      + '<div class="msg-col">'
      + '  <div class="bubble">' + html + '</div>'
      + '  <div class="msg-time">' + time + '</div>'
      + feedback
      + '</div>';

    container.appendChild(row);
    wireFeedback(row);
    return row;
  }

  function wireFeedback(row) {
    var buttons = row.querySelectorAll(".msg-feedback button");
    buttons.forEach(function (btn) {
      btn.addEventListener("click", function () {
        var group = btn.closest(".msg-feedback");
        group.querySelectorAll("button").forEach(function (b) { b.classList.remove("active"); });
        btn.classList.add("active");
        var messageId = group.getAttribute("data-message-id");
        ASKMQL.api.feedback.submit(messageId, btn.getAttribute("data-rating")).then(function () {
          ASKMQL.ui.toast.show("Thanks for the feedback!");
        });
      });
    });
  }

  function showTyping(container) {
    var row = document.createElement("div");
    row.className = "msg-row ai typing-row";
    row.id = "typingRow";
    row.innerHTML = ''
      + '<div class="msg-avatar ai">' + icon("book-bookmark") + '</div>'
      + '<div class="msg-col"><div class="bubble">'
      + '<span class="typing-dot"></span><span class="typing-dot"></span><span class="typing-dot"></span>'
      + '</div></div>';
    container.appendChild(row);
    return row;
  }

  function hideTyping(container) {
    var row = container.querySelector("#typingRow");
    if (row) row.remove();
  }

  return { render: render, showTyping: showTyping, hideTyping: hideTyping };
})();
