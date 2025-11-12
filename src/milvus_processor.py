import os
from typing import List
from dotenv import load_dotenv
from pymilvus import MilvusClient
from src.embedder import Embedder
from src.decorator import singleton


class MilvusProcessor:

    def __init__(self, embedder: Embedder, database_path: str, collection_name: str = "valve"):
        self.milvus_client = MilvusClient(uri=database_path)
        self.embedder = embedder
        self.collection_name = collection_name
        self.database_path = database_path
        load_dotenv()
        if not self.milvus_client.has_collection(collection_name=collection_name):
            raise ValueError(f"Collection {collection_name} does not exist in Milvus Lite instance {database_path}")

    def get_data(self, query_text: str, limit: int = int(os.getenv("MILVUS_MAX_RESULTS", 10)), distance_threshold: float = float(os.getenv("EMBEDDING_THRESHOLD", -1.0))) -> List[str]:
        embeddings = self.embedder.encode(query_text)
        search_results_raw = self.milvus_client.search(collection_name=self.collection_name, data=[embeddings], limit=limit, output_fields=["text"])[0]
        search_results_raw = [hit for hit in search_results_raw[0] if hit['distance'] > distance_threshold] if 0 < distance_threshold < 1 else search_results_raw
        return [hit['entity']['text'] for hit in search_results_raw]
