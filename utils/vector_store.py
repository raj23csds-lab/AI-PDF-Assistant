from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from utils.embeddings import get_embedding_model


def create_vector_store(chunks):

    embedding_model = get_embedding_model()

    documents = []

    for chunk in chunks:

        documents.append(
            Document(
    page_content=chunk["text"],
    metadata={
        "source": chunk["source"],
        "page": chunk["page"]
    }
))

    vector_store = FAISS.from_documents(
        documents,
        embedding_model
    )

    return vector_store


def save_vector_store(vector_store):

    vector_store.save_local("vectorstore")


def load_vector_store():

    embedding_model = get_embedding_model()

    return FAISS.load_local(
        "vectorstore",
        embedding_model,
        allow_dangerous_deserialization=True
    )