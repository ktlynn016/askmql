"""Login/signup/logout logic. Session state itself (who's currently
logged in) is stored in Flask's signed, httpOnly session cookie --
never in any client-side JS storage -- so controllers only ever touch
this module's functions plus flask.session, never models directly.
"""
from flask import session

from models.user import ROLE_STUDENT, ROLE_LIBRARIAN
from repositories.user_repository import UserRepository
from core.errors import ValidationError, UnauthorizedError

_repo = UserRepository()


def signup_student(name, student_id, department, password):
    if not name or not student_id or not password:
        raise ValidationError("name, student_id, and password are required")
    if len(password) < 8:
        raise ValidationError("password must be at least 8 characters")
    if _repo.get_by_student_id(student_id):
        raise ValidationError("An account with that student ID already exists")

    initials = "".join(part[0] for part in name.split()[:2]).upper() or "ST"
    user = _repo.create(
        name=name,
        role=ROLE_STUDENT,
        student_id=student_id,
        department=department,
        avatar_initials=initials,
    )
    user.set_password(password)
    _repo._commit()

    _start_session(user)
    return user


def login(identifier, password, expected_role=None):
    """`identifier` is a student_id for students, an email for
    librarians. `expected_role`, if given, rejects a correct password
    on the wrong account type (e.g. a student ID typed into the
    librarian tab)."""
    if not identifier or not password:
        raise ValidationError("identifier and password are required")

    user = _repo.get_by_student_id(identifier) or _repo.get_by_email(identifier)
    if not user or not user.check_password(password):
        raise UnauthorizedError("Invalid credentials")
    if expected_role and user.role != expected_role:
        raise UnauthorizedError("Invalid credentials")

    _start_session(user)
    return user


def logout():
    session.clear()


def current_user():
    user_id = session.get("user_id")
    if not user_id:
        return None
    return _repo.get(user_id)


def _start_session(user):
    session.clear()
    session["user_id"] = user.id
    session["role"] = user.role
