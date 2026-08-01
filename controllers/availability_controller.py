from flask import jsonify, request

from services.catalog import availability_service


def get_availability(book_id):
    return jsonify(availability_service.get_availability(book_id))


def put_availability(book_id):
    data = request.get_json(silent=True) or {}
    return jsonify(availability_service.set_availability(book_id, bool(data.get("available"))))
