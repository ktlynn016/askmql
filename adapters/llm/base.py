"""Interface every LLM adapter must implement.

services/generation/llm_client.py depends only on this, never on a
concrete provider -- so swapping providers means adding one file here
and flipping core.config.Config.LLM_PROVIDER.
"""
from abc import ABC, abstractmethod


class LLMAdapter(ABC):
    @abstractmethod
    def complete(self, system_prompt: str, user_prompt: str) -> str:
        """Return a plain-text completion for the given prompts."""
        raise NotImplementedError
