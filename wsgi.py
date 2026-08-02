"""WSGI entry point for production servers (gunicorn wsgi:app, or
whatever Render/Railway/PythonAnywhere expects)."""
from app import app

if __name__ == "__main__":
    app.run()
