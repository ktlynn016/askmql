from flask import Blueprint

from controllers import feedback_controller

feedback_bp = Blueprint("feedback", __name__)
feedback_bp.route("/feedback", methods=["POST"])(feedback_controller.post_feedback)
