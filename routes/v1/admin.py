from flask import Blueprint

from controllers import admin_controller
from core.security import require_role
from models.user import ROLE_LIBRARIAN

admin_bp = Blueprint("admin", __name__)
admin_bp.route("/admin/metrics", methods=["GET"])(require_role(ROLE_LIBRARIAN)(admin_controller.get_metrics))
admin_bp.route("/admin/sync-catalog", methods=["POST"])(
    require_role(ROLE_LIBRARIAN)(admin_controller.post_sync_catalog)
)
