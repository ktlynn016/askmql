/* In-memory app state: conversations + the current login session. No
   localStorage/sessionStorage is used (kept out deliberately), so
   this resets on every page load/navigation -- acceptable for an
   offline demo prototype, and clearly documented as such (see
   frontend/README.md). Wiring ASKMQL.core.constants.USE_API to the
   real backend is what makes both conversation history AND login
   persist for real, since a real browser session cookie is not a JS
   storage API and survives page navigation on its own. */
ASKMQL.state.store = (function () {
  var conversations = [
    { id: "c1", title: "AI book recommendations", messages: [] }
  ];
  var activeConversationId = conversations[0].id;

  // null = not logged in (this page load). See module docstring above
  // for why this doesn't survive navigation in offline mode.
  var session = null;

  function listConversations() { return conversations; }

  function getActiveId() { return activeConversationId; }
  function setActiveId(id) { activeConversationId = id; }

  function getConversation(id) {
    var found = null;
    conversations.forEach(function (c) { if (c.id === id) found = c; });
    return found;
  }

  function createConversation(title) {
    var conv = { id: "c" + Date.now(), title: title || "New conversation", messages: [] };
    conversations.unshift(conv);
    activeConversationId = conv.id;
    return conv;
  }

  function renameConversation(id, title) {
    var conv = getConversation(id);
    if (conv) conv.title = title;
    return conv;
  }

  function deleteConversation(id) {
    conversations = conversations.filter(function (c) { return c.id !== id; });
    if (activeConversationId === id) {
      activeConversationId = conversations.length ? conversations[0].id : null;
    }
  }

  function addMessage(conversationId, role, html) {
    var conv = getConversation(conversationId);
    if (!conv) return;
    conv.messages.push({ role: role, html: html, ts: new Date() });
  }

  function getSession() { return session; }
  function setSession(user) { session = user; }
  function clearSession() { session = null; }

  return {
    listConversations: listConversations,
    getActiveId: getActiveId,
    setActiveId: setActiveId,
    getConversation: getConversation,
    createConversation: createConversation,
    renameConversation: renameConversation,
    deleteConversation: deleteConversation,
    addMessage: addMessage,
    getSession: getSession,
    setSession: setSession,
    clearSession: clearSession
  };
})();
