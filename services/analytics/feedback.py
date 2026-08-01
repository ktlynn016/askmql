from repositories.feedback_repository import FeedbackRepository

_repo = FeedbackRepository()


def submit(message_id, rating, note=None):
    if rating not in ("up", "down"):
        from core.errors import ValidationError

        raise ValidationError("rating must be 'up' or 'down'")
    return _repo.create(message_id, rating, note=note)
