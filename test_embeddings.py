from utils.embeddings import get_embedding_model

embedding_model = get_embedding_model()

embedding = embedding_model.embed_query(
    "Artificial Intelligence is changing the world."
)

print("Embedding Length:", len(embedding))
print(embedding[:10])