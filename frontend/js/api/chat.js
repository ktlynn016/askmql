/* Sends a chat message and gets a reply -- dummy mode replicates
   backend/services/chat/orchestrator.py's shape (reply/books/
   announcements/conversation_id) so swapping USE_API doesn't change
   how callers use the response. */
ASKMQL.api.chat = (function () {
  var USE_API = ASKMQL.core.constants.USE_API;
  var store = ASKMQL.state.store;

  function localReply(text) {
    var textL = text.toLowerCase();
    if (textL.indexOf("announce") !== -1) {
      return ASKMQL.api.announcements.list().then(function (announcements) {
        return { reply: "Here are today's library announcements.", books: [], announcements: announcements };
      });
    }
    return ASKMQL.api.books.search(text).then(function (matches) {
      if (matches.length) {
        return { reply: "Here's what I found in the catalog:", books: matches.slice(0, 4), announcements: [] };
      }
      return {
        reply: "I couldn't find an exact match for that in the sample catalog yet. Try asking about AI, programming, databases, or networking books — or tell me a title or author to search for.",
        books: [], announcements: []
      };
    });
  }

  function sendMessage(text, conversationId) {
    if (USE_API) {
      return ASKMQL.api.client.post("/chat", { message: text, conversation_id: conversationId });
    }
    return localReply(text).then(function (result) {
      result.conversation_id = conversationId;
      return result;
    });
  }

  return { sendMessage: sendMessage };
})();
