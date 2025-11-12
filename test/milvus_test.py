from pymilvus import MilvusClient
from sentence_transformers import SentenceTransformer


MODEL_NAME="sentence-transformers/distiluse-base-multilingual-cased-v2"
embedding_model = SentenceTransformer('/home/mrglaster/.cache/huggingface/hub/models--sentence-transformers--distiluse-base-multilingual-cased-v2/snapshots/bfe45d0732ca50787611c0fe107ba278c7f3f889')
milvus_client = MilvusClient(uri="../database/hlr-distiluse-cv2-1.0.db")
collection_name = "valve"

query_text = "Как сделать оружие с помощью Half-Life Weapon Mod?"
query_embedding = embedding_model.encode(query_text).tolist()

search_results = milvus_client.search(
        collection_name=collection_name,
        data=[query_embedding],
        limit=5,
        output_fields=["text"]
)
print(search_results)
print("Search results:")
for hit in search_results[0]:
    print(f"Text: {hit['entity']['text']}, Distance: {hit['distance']:.4f}")

