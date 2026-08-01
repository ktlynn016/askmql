"""Real LLM adapter stub -- NOT wired in by default.

Fill in the API call and set LLM_PROVIDER=anthropic (and an API key
env var of your choice) to activate. Left unimplemented on purpose so
this repo has no hidden network calls or cost until you opt in.
"""
from adapters.llm.base import LLMAdapter
from core.errors import UpstreamServiceError


class AnthropicAdapter(LLMAdapter):
    def __init__(self, api_key: str, model: str = "claude-sonnet-4-6"):
        self.api_key = api_key
        self.model = model

    def complete(self, system_prompt: str, user_prompt: str) -> str:
        raise UpstreamServiceError(
            "AnthropicAdapter is a stub -- implement the API call in "
            "adapters/llm/anthropic_adapter.py before selecting "
            "LLM_PROVIDER=anthropic."
        )
