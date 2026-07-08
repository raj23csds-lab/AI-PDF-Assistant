from utils.chunk_text import split_text
from utils.vector_store import (
    create_vector_store,
    save_vector_store,
    load_vector_store
)

sample_text = """
Artificial Intelligence is transforming industries.
Machine Learning learns from data.
Deep Learning uses neural networks.
Generative AI creates content.
""" * 100

chunks = split_text(sample_text)

print("Chunks:", len(chunks))

vector_store = create_vector_store(chunks)

save_vector_store(vector_store)

print("✅ Vector Store Saved!")

loaded_store = load_vector_store()

results = loaded_store.similarity_search(
    "What is Deep Learning?",
    k=2
)

print("\nRetrieved Results:\n")

for i, doc in enumerate(results, start=1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 50)