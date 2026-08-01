from flask import Blueprint

from controllers import availability_controller

availability_bp = Blueprint("availability", __name__)
availability_bp.route("/books/<int:book_id>/availability", methods=["GET"])(
    availability_controller.get_availability
)
availability_bp.route("/books/<int:book_id>/availability", methods=["PUT"])(
    availability_controller.put_availability
)
