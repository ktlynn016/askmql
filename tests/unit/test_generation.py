import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))

from services.generation import validator


def test_validator_trims_whitespace():
    assert validator.validate("  hello world  ") == "hello world"


def test_validator_handles_empty():
    assert validator.validate("") == "I'm not sure how to answer that yet."


def test_validator_truncates_long_text():
    long_text = "a" * 3000
    result = validator.validate(long_text)
    assert len(result) <= 2001
    assert result.endswith("…")
