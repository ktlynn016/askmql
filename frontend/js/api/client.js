/* Thin fetch wrapper for the real backend. Only used when
   ASKMQL.core.constants.USE_API is true -- see backend/README.md. */
ASKMQL.api = ASKMQL.api || {};

ASKMQL.api.client = (function () {
  var BASE = ASKMQL.core.constants.API_BASE_URL;

  function request(path, options) {
    return fetch(BASE + path, Object.assign({
      headers: { "Content-Type": "application/json" },
      credentials: "include"  // sends/receives the auth session cookie; not a JS storage API
    }, options || {})).then(function (res) {
      if (!res.ok) throw new Error("API error " + res.status + " on " + path);
      if (res.status === 204) return null;
      return res.json();
    });
  }

  return {
    get: function (path) { return request(path, { method: "GET" }); },
    post: function (path, body) { return request(path, { method: "POST", body: JSON.stringify(body) }); },
    patch: function (path, body) { return request(path, { method: "PATCH", body: JSON.stringify(body) }); },
    del: function (path) { return request(path, { method: "DELETE" }); }
  };
})();
