"""Unit test for services/chat/intent.py -- no DB/app context needed."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from services.chat import intent


def test_classifies_announcements():
    assert intent.classify("Tell me today's library announcements") == intent.INTENT_ANNOUNCEMENTS
    assert intent.classify("Any announcements?") == intent.INTENT_ANNOUNCEMENTS


def test_classifies_search_by_default():
    assert intent.classify("Is Clean Code available?") == intent.INTENT_SEARCH
    assert intent.classify("Recommend programming books") == intent.INTENT_SEARCH
