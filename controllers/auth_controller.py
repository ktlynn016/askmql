from flask import jsonify, request

from services.auth import auth_service
from models.user import ROLE_STUDENT, ROLE_LIBRARIAN


def post_signup():
    data = request.get_json(silent=True) or {}
    user = auth_service.signup_student(
        data.get("name"),
        data.get("student_id"),
        data.get("department"),
        data.get("password"),
    )
    return jsonify(user.to_dict()), 201


def post_login():
    data = request.get_json(silent=True) or {}
    role = data.get("role")  # "student" | "librarian", optional but recommended
    expected_role = {"student": ROLE_STUDENT, "librarian": ROLE_LIBRARIAN}.get(role)
    user = auth_service.login(data.get("identifier"), data.get("password"), expected_role=expected_role)
    return jsonify(user.to_dict())


def post_logout():
    auth_service.logout()
    return "", 204


def get_me():
    user = auth_service.current_user()
    if not user:
        return jsonify({"user": None}), 200
    return jsonify(user.to_dict())
