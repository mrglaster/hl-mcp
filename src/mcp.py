from pydantic import ValidationError
from src.decorator import singleton
from src.milvus_processor import MilvusProcessor


@singleton
class MCPProcessor:
    __milvus_processor = None

    def __init__(self, milvus_processor: MilvusProcessor):
        self.__milvus_processor = milvus_processor

    @property
    def milvus_processor(self):
        return self.__milvus_processor

    def get_assistant_data(self, milvus_query: str):
        """Retrieves data from Milvus vector databases and returns it"""
        extracted_data = self.__milvus_processor.get_data(query_text=milvus_query)
        return extracted_data
