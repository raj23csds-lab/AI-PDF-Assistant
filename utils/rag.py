from langchain_core.prompts import ChatPromptTemplate

from utils.vector_store import load_vector_store
from utils.chatbot import get_llm


def ask_question(question):

    vector_store = load_vector_store()

    docs = vector_store.similarity_search(
        question,
        k=4
    )

    context = "\n\n".join(
        doc.page_content for doc in docs
    )

    prompt = ChatPromptTemplate.from_template(
        """
You are an intelligent AI assistant.

Answer ONLY using the information provided in the context.

If the answer is not found in the context, reply exactly:

"I couldn't find this information in the uploaded PDF."

Context:
{context}

Question:
{question}

Answer:
"""
    )

    llm = get_llm()

    chain = prompt | llm

    response = chain.invoke(
        {
            "context": context,
            "question": question
        }
    )

    return response.content, docs