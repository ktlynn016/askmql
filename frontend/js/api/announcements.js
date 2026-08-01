ASKMQL.api.announcements = (function () {
  var data = ASKMQL.state.catalogData;
  var USE_API = ASKMQL.core.constants.USE_API;

  function list() {
    if (USE_API) return ASKMQL.api.client.get("/announcements").then(function (items) {
      return items.map(function (a) { return a.message; });
    });
    return Promise.resolve(data.ANNOUNCEMENTS);
  }

  return { list: list };
})();
