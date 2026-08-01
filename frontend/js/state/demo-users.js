/* Demo credential store for OFFLINE mode only (USE_API=false).
   Plaintext password comparison here is fine ONLY because this is a
   client-side demo with no real secrets -- it is NOT how real auth
   works. The actual backend (services/auth/auth_service.py) always
   hashes passwords with Werkzeug and never sends them back to the
   client. When USE_API=true, this file isn't used at all -- real
   login goes through js/api/client.js against the Flask session. */
ASKMQL.state.demoUsers = (function () {
  var students = [
    { student_id: "2023-0114", password: "student123", name: "Jamie Cruz", role: "student", department: "BSIT", avatar_initials: "JC" }
  ];
  var librarians = [
    { email: "librarian@gsu-mosqueda.edu.ph", password: "librarian123", name: "Maria Santos", role: "librarian", department: "Library Staff", avatar_initials: "MS" }
  ];

  function toPublic(u) {
    return {
      name: u.name, role: u.role, email: u.email || null,
      student_id: u.student_id || null, department: u.department, avatar_initials: u.avatar_initials
    };
  }

  function findStudent(studentId) {
    return students.filter(function (s) { return s.student_id === studentId; })[0] || null;
  }
  function findLibrarian(email) {
    return librarians.filter(function (l) { return l.email === email; })[0] || null;
  }

  function check(identifier, password, role) {
    var candidate = findStudent(identifier) || findLibrarian(identifier);
    if (!candidate) return null;
    if (role && candidate.role !== role) return null;
    if (candidate.password !== password) return null;
    return toPublic(candidate);
  }

  function addStudent(data) {
    var initials = (data.name || "Student").trim().split(/\s+/).slice(0, 2)
      .map(function (w) { return w[0]; }).join("").toUpperCase();
    var user = {
      student_id: data.student_id, password: data.password, name: data.name,
      role: "student", department: data.department || "", avatar_initials: initials || "ST"
    };
    students.push(user);
    return toPublic(user);
  }

  return { findStudent: findStudent, findLibrarian: findLibrarian, check: check, addStudent: addStudent };
})();
