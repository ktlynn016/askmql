ASKMQL.api.conversations = (function () {
  var store = ASKMQL.state.store;
  var USE_API = ASKMQL.core.constants.USE_API;

  function list() {
    if (USE_API) return ASKMQL.api.client.get("/conversations");
    return Promise.resolve(store.listConversations());
  }

  function create(title) {
    if (USE_API) return ASKMQL.api.client.post("/conversations", { title: title });
    return Promise.resolve(store.createConversation(title));
  }

  function rename(id, title) {
    if (USE_API) return ASKMQL.api.client.patch("/conversations/" + id, { title: title });
    return Promise.resolve(store.renameConversation(id, title));
  }

  function remove(id) {
    if (USE_API) return ASKMQL.api.client.del("/conversations/" + id);
    store.deleteConversation(id);
    return Promise.resolve();
  }

  function messages(id) {
    if (USE_API) return ASKMQL.api.client.get("/conversations/" + id + "/messages");
    var conv = store.getConversation(id);
    return Promise.resolve(conv ? conv.messages : []);
  }

  return { list: list, create: create, rename: rename, remove: remove, messages: messages };
})();
