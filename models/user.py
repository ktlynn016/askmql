from werkzeug.security import generate_password_hash, check_password_hash

from database.db import db

ROLE_STUDENT = "student"
ROLE_LIBRARIAN = "librarian"


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    role = db.Column(db.Enum(ROLE_STUDENT, ROLE_LIBRARIAN, name="user_role"), nullable=False, default=ROLE_STUDENT)
    email = db.Column(db.String(150), unique=True, nullable=True)
    password_hash = db.Column(db.String(255), nullable=True)
    student_id = db.Column(db.String(30), unique=True, nullable=True)
    department = db.Column(db.String(100))
    avatar_initials = db.Column(db.String(4))

    def set_password(self, raw_password):
        self.password_hash = generate_password_hash(raw_password)

    def check_password(self, raw_password):
        if not self.password_hash:
            return False
        return check_password_hash(self.password_hash, raw_password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "role": self.role,
            "email": self.email,
            "student_id": self.student_id,
            "department": self.department,
            "avatar_initials": self.avatar_initials,
        }
