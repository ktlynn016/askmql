from flask import Blueprint

from controllers import book_controller

books_bp = Blueprint("books", __name__)
books_bp.route("/books", methods=["GET"])(book_controller.get_books)
books_bp.route("/books/<int:book_id>", methods=["GET"])(book_controller.get_book)
books_bp.route("/recommendations", methods=["GET"])(book_controller.get_recommendations)
