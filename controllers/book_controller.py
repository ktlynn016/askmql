from flask import jsonify, request

from services.catalog import book_service


def get_books():
    query = request.args.get("q")
    category = request.args.get("category")
    books = book_service.list_books(query=query, category=category)
    return jsonify([b.to_dict() for b in books])


def get_book(book_id):
    book = book_service.get_book(book_id)
    return jsonify(book.to_dict(include_related=True))


def get_recommendations():
    category = request.args.get("category")
    books = book_service.recommend(category=category)
    return jsonify([b.to_dict() for b in books])
