from flask import Blueprint

from controllers import announcement_controller

announcements_bp = Blueprint("announcements", __name__)
announcements_bp.route("/announcements", methods=["GET"])(
    announcement_controller.get_announcements
)
