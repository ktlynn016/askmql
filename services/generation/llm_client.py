"""Thin wrapper around the configured LLM adapter (see
adapters/llm/factory.py). This is the only file services/chat should
import to get text back from "the model" -- keeps provider swaps and
prompt-building changes independent of each other."""
from adapters.llm.factory import get_llm_adapter

_adapter = get_llm_adapter()


def generate(system_prompt: str, user_prompt: str) -> str:
    return _adapter.complete(system_prompt, user_prompt)
