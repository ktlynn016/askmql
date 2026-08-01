"""Default LLM adapter: no external API call at all.

Produces a deterministic, template-based reply from whatever context
services/generation/prompt_builder.py assembled. This is what keeps
the whole system runnable today with zero API keys and zero cost --
swap LLM_PROVIDER=anthropic (or similar) once real generation is
wanted; nothing above this layer needs to change.
"""
from adapters.llm.base import LLMAdapter


class TemplateAdapter(LLMAdapter):
    def complete(self, system_prompt: str, user_prompt: str) -> str:
        # The prompt builder already produced a good plain-text answer;
        # a real LLM adapter would send system_prompt + user_prompt to
        # a model and return its text instead of just echoing it back.
        return user_prompt
