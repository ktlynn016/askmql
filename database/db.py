"""Shared SQLAlchemy instance, imported by models/*.py and initialized
against the Flask app in app.py."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
