from flask import Blueprint

from controllers import conversation_controller

conversations_bp = Blueprint("conversations", __name__)
conversations_bp.route("/conversations", methods=["GET"])(conversation_controller.get_conversations)
conversations_bp.route("/conversations", methods=["POST"])(conversation_controller.post_conversation)
conversations_bp.route("/conversations/<int:conversation_id>", methods=["PATCH"])(
    conversation_controller.patch_conversation
)
conversations_bp.route("/conversations/<int:conversation_id>", methods=["DELETE"])(
    conversation_controller.delete_conversation
)
conversations_bp.route("/conversations/<int:conversation_id>/messages", methods=["GET"])(
    conversation_controller.get_messages
)
