from core.config import Config
from adapters.llm.template_adapter import TemplateAdapter
from adapters.llm.anthropic_adapter import AnthropicAdapter


def get_llm_adapter():
    if Config.LLM_PROVIDER == "anthropic":
        return AnthropicAdapter(api_key="")  # wire up a real key/env var when ready
    return TemplateAdapter()
