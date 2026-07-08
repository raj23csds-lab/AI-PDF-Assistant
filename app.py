import os
import time
import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.chunk_text import split_text
from utils.vector_store import create_vector_store, save_vector_store
from utils.rag import ask_question

st.set_page_config(
    page_title="Multi PDF Chatbot using RAG",
    page_icon="📄",
    layout="wide"
)


def load_css():
    with open("assets/style.css", "r", encoding="utf-8") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )


load_css()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "processed" not in st.session_state:
    st.session_state.processed = False

st.markdown(
    """
    <div class="main-title">
        🤖 AI PDF Assistant
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
        Multi-PDF • Gemini 2.5 • FAISS • RAG
    </div>
    """,
    unsafe_allow_html=True
)

with st.sidebar:

    st.header("📂 Upload PDFs")

    uploaded_files = st.file_uploader(
        "Choose PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if uploaded_files:
        st.success(f"📄 {len(uploaded_files)} PDF(s) selected")

    if st.button("🚀 Process PDFs"):

        if uploaded_files:

            with st.spinner("Processing PDFs..."):

                os.makedirs("uploads", exist_ok=True)

                chunks = []

                for uploaded_file in uploaded_files:

                    pdf_path = os.path.join(
                        "uploads",
                        uploaded_file.name
                    )

                    with open(pdf_path, "wb") as f:
                        f.write(uploaded_file.getbuffer())

                    pages = extract_text_from_pdf(pdf_path)

                    chunks.extend(
                        split_text(
                            pages,
                            uploaded_file.name
                        )
                    )

                vector_store = create_vector_store(chunks)

                save_vector_store(vector_store)

                st.session_state.processed = True
                st.session_state.messages = []

            st.success(
                f"✅ {len(uploaded_files)} PDF(s) processed successfully!"
            )

        else:
            st.warning("Please upload at least one PDF.")

    st.divider()

    if st.button("🗑 Clear Chat"):

        st.session_state.messages = []
        st.rerun()

pdf_count = len(uploaded_files) if uploaded_files else 0

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("📄 PDFs", pdf_count)

with col2:
    st.metric("🤖 LLM", "Gemini 2.5")

with col3:
    st.metric("🧠 Vector DB", "FAISS")

with col4:
    st.metric("⚡ Pipeline", "RAG")

st.divider()

for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if st.session_state.processed:

    question = st.chat_input(
        "Ask anything about your uploaded PDFs..."
    )

    if question:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        with st.chat_message("user"):
            st.markdown(question)

        with st.chat_message("assistant"):

            answer, docs = ask_question(question)

            placeholder = st.empty()

            response = ""

            for word in answer.split():

                response += word + " "

                placeholder.markdown(response)

                time.sleep(0.02)

            with st.expander("📑 Retrieved Context"):

                for i, doc in enumerate(docs, start=1):

                    source = doc.metadata.get(
                        "source",
                        "Unknown PDF"
                    )

                    page = doc.metadata.get(
                        "page",
                        "Unknown"
                    )

                    st.markdown(
                        f"### 📄 {source} | Page {page}"
                    )

                    st.write(doc.page_content)

                    st.divider()

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

else:

    st.info(
        "👈 Upload one or more PDFs and click **Process PDFs** to start chatting."
    )