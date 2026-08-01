"""Unit test for password hashing on the User model -- no DB/app
context needed, since set_password/check_password are pure Werkzeug
calls plus attribute assignment."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from models.user import User


def test_password_hash_roundtrip():
    user = User(name="Test Student")
    user.set_password("student123")
    assert user.password_hash != "student123"
    assert user.check_password("student123") is True
    assert user.check_password("wrong-password") is False


def test_check_password_without_hash_set():
    user = User(name="No Password Yet")
    assert user.check_password("anything") is False
