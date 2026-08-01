ASKMQL.api.feedback = (function () {
  var USE_API = ASKMQL.core.constants.USE_API;

  function submit(messageId, rating, note) {
    if (USE_API) {
      return ASKMQL.api.client.post("/feedback", { message_id: messageId, rating: rating, note: note || null });
    }
    // Dummy mode: nothing to persist server-side; resolve so the UI
    // can still show a confirmation.
    return Promise.resolve({ message_id: messageId, rating: rating });
  }

  return { submit: submit };
})();
