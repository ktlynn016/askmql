from flask import jsonify

from repositories.announcement_repository import AnnouncementRepository

_repo = AnnouncementRepository()


def get_announcements():
    return jsonify([a.to_dict() for a in _repo.list()])
