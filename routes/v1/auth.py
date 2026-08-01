from flask import Blueprint

from controllers import auth_controller

auth_bp = Blueprint("auth", __name__)
auth_bp.route("/auth/signup", methods=["POST"])(auth_controller.post_signup)
auth_bp.route("/auth/login", methods=["POST"])(auth_controller.post_login)
auth_bp.route("/auth/logout", methods=["POST"])(auth_controller.post_logout)
auth_bp.route("/auth/me", methods=["GET"])(auth_controller.get_me)
