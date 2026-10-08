# 🤖 AI PDF Assistant using RAG

An AI-powered PDF chatbot that allows users to upload one or multiple PDF documents and ask questions in natural language. The application uses Retrieval-Augmented Generation (RAG) with Google Gemini and FAISS to provide accurate, context-aware answers from uploaded documents.
 
---

## 🚀 Live Demo

🔗https://smartpdf-assistant.streamlit.app/

---
## ✨ Features

- 📄 Upload multiple PDF files
- 🤖 Ask questions in natural language
- 🧠 Google Gemini 2.5 Flash
- 🔍 Semantic Search using FAISS
- 📚 Retrieval-Augmented Generation (RAG)
- 📑 Displays source PDF and page number
- 💬 Interactive chat interface
- ⚡ Fast document retrieval
- ☁️ Streamlit Cloud Deployment

---

## 🏗️ Project Architecture

```
User
   │
   ▼
Upload PDFs
   │
   ▼
Text Extraction
   │
   ▼
Chunking
   │
   ▼
Embeddings
   │
   ▼
FAISS Vector Database
   │
   ▼
Retriever
   │
   ▼
Google Gemini
   │
   ▼
Answer with Citations
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / LLM

- Google Gemini 2.5 Flash
- LangChain

### Vector Database

- FAISS

### Embeddings

- HuggingFace
- sentence-transformers

### PDF Processing

- PyPDF

---

## 📂 Folder Structure

```
AI-PDF-Assistant
│
├── app.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
│
├── assets
│   └── style.css
│
├── utils
│   ├── chatbot.py
│   ├── chunk_text.py
│   ├── embeddings.py
│   ├── pdf_reader.py
│   ├── rag.py
│   └── vector_store.py
│
├── data
└── uploads
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-PDF-Assistant.git
```

Go to the project

```bash
cd AI-PDF-Assistant
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment

Windows

```bash
venv\Scripts\activate
```

Install Dependencies

```bash
pip install -r requirements.txt
```

Create `.env`

```
GOOGLE_API_KEY=YOUR_API_KEY
```

Run

```bash
streamlit run app.py
```

---

## 📈 Future Enhancements

- OCR Support
- Voice Input
- Voice Output
- AI Generated PDF Summary
- Conversation Memory
- Chat Export (PDF/TXT)
- Dark Mode
- Docker Deployment

---

## 👩‍💻 Author

**Rakshitha J**

Computer Science Engineering (Data Science)

GitHub:
https://github.com/raj23csds-lab


---


