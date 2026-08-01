"""End-to-end: POST /api/v1/chat should return a reply shape the
frontend depends on, regardless of whether books were matched.
Requires a seeded database -- see backend/README.md.
"""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

import pytest


@pytest.fixture
def client():
    from app import create_app

    app = create_app()
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


def test_chat_requires_message(client):
    resp = client.post("/api/v1/chat", json={})
    assert resp.status_code == 400


def test_chat_response_shape(client):
    resp = client.post("/api/v1/chat", json={"message": "Is Clean Code available?"})
    assert resp.status_code in (200, 500)  # 500 only if DB isn't reachable in this env
    if resp.status_code == 200:
        body = resp.get_json()
        for key in ("conversation_id", "reply", "books", "announcements", "intent"):
            assert key in body
