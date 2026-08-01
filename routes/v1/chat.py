from flask import Blueprint

from controllers import chat_controller

chat_bp = Blueprint("chat", __name__)
chat_bp.route("/chat", methods=["POST"])(chat_controller.post_chat)
