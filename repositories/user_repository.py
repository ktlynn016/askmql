from models.user import User
from repositories.base import BaseRepository


class UserRepository(BaseRepository):
    def get(self, user_id):
        return User.query.get(user_id)

    def get_by_student_id(self, student_id):
        return User.query.filter_by(student_id=student_id).first()

    def get_by_email(self, email):
        return User.query.filter_by(email=email).first()

    def create(self, **fields):
        user = User(**fields)
        self._add(user)
        self._commit()
        return user
