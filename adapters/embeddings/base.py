from abc import ABC, abstractmethod


class EmbeddingsAdapter(ABC):
    @abstractmethod
    def embed(self, texts: list) -> list:
        """Return a list of embedding vectors, one per input text."""
        raise NotImplementedError
