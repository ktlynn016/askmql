/* Login/signup/logout/me -- dual mode like every other file in
   js/api/. Real mode relies entirely on the browser's own cookie jar
   (via credentials:"include" in client.js) for persistence, never on
   any JS storage API. Dummy mode checks js/state/demo-users.js and
   keeps the "session" in js/state/store.js for the current page only. */
ASKMQL.api.auth = (function () {
  var USE_API = ASKMQL.core.constants.USE_API;
  var store = ASKMQL.state.store;
  var demo = ASKMQL.state.demoUsers;

  function signupStudent(data) {
    if (USE_API) {
      return ASKMQL.api.client.post("/auth/signup", data).then(function (user) {
        store.setSession(user);
        return user;
      });
    }
    if (!data.name || !data.student_id || !data.password) {
      return Promise.reject(new Error("Name, student ID, and password are required."));
    }
    if (data.password.length < 8) {
      return Promise.reject(new Error("Password must be at least 8 characters."));
    }
    if (demo.findStudent(data.student_id)) {
      return Promise.reject(new Error("An account with that student ID already exists."));
    }
    var user = demo.addStudent(data);
    store.setSession(user);
    return Promise.resolve(user);
  }

  function login(identifier, password, role) {
    if (USE_API) {
      return ASKMQL.api.client.post("/auth/login", { identifier: identifier, password: password, role: role })
        .then(function (user) {
          store.setSession(user);
          return user;
        })
        .catch(function () { throw new Error("Invalid credentials."); });
    }
    var user = demo.check(identifier, password, role);
    if (!user) return Promise.reject(new Error("Invalid credentials."));
    store.setSession(user);
    return Promise.resolve(user);
  }

  function logout() {
    store.clearSession();
    if (USE_API) return ASKMQL.api.client.post("/auth/logout", {});
    return Promise.resolve();
  }

  function me() {
    if (USE_API) {
      return ASKMQL.api.client.get("/auth/me").then(function (res) {
        if (res && res.user) store.setSession(res.user);
        else store.clearSession();
        return res ? res.user : null;
      });
    }
    return Promise.resolve(store.getSession());
  }

  return { signupStudent: signupStudent, login: login, logout: logout, me: me };
})();
