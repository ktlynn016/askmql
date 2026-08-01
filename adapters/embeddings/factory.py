from core.config import Config
from adapters.embeddings.none_adapter import NoneAdapter


def get_embeddings_adapter():
    # Add real providers (OpenAI, Voyage, local sentence-transformers,
    # etc.) here as EMBEDDINGS_PROVIDER options grow.
    if Config.EMBEDDINGS_PROVIDER == "none":
        return NoneAdapter()
    return NoneAdapter()
