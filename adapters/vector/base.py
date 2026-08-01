from abc import ABC, abstractmethod


class VectorStoreAdapter(ABC):
    @abstractmethod
    def upsert(self, ids: list, vectors: list, metadata: list):
        raise NotImplementedError

    @abstractmethod
    def query(self, vector, top_k: int):
        """Return a list of (id, score) tuples, best first."""
        raise NotImplementedError
