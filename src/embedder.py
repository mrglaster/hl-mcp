from typing import List
from sentence_transformers import SentenceTransformer
from src.decorator import singleton


@singleton
class Embedder:
    """Class providing interface to work with the embedding model"""
    def __init__(self, model_name: str):
        self.embedding_model = SentenceTransformer(model_name_or_path=model_name)

    def encode(self, text: str) -> List:
        """Turns text provided to list of embeddings"""
        return self.embedding_model.encode(text).tolist()