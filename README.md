# 🧠 RAG Wikipedia Assistant

A **Retrieval-Augmented Generation (RAG)** system that answers questions using real **Wikipedia knowledge** — not just the model’s internal data.

It combines:
- 🌐 Wikipedia Scraping  
- ✂️ Text Chunking  
- 🧠 Embedding & Vector Search (FAISS)  
- 💬 Context-Aware Answer Generation (LangChain + Gemini)

---

## 🎯 Project Goal

Provide **fact-based, verifiable answers** by retrieving relevant Wikipedia text before generating a response — reducing hallucinations and improving factual accuracy.

---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Ramee4sure/RAG-Wikipedia-Assitant.git
cd RAG-Wikipedia-Assitant
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
.venv\Scripts\activate      # On Windows
source .venv/bin/activate     # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

The assistant automatically creates `.env_example` on first run if it doesn’t exist.  
You can also create or edit it manually:

```bash
# Example environment variables for RAG Wikipedia Assistant

GOOGLE_API_KEY="YOUR_GEMINI_API_KEY"
WIKIPEDIA_TOPIC="Artificial Intelligence"
CHUNK_SIZE=500
CHUNK_OVERLAP=100
```

(Optional)
```bash
cp .env_example .env
```

---

### 5️⃣ Run the Assistant

```bash
python src/app.py
```

The assistant will:

1. 🕸️ Scrape a Wikipedia topic  
2. ✂️ Split the text into chunks  
3. 🧬 Generate embeddings  
4. 🗂️ Build a FAISS vector store  
5. 🔍 Retrieve the most relevant context  
6. 💡 Generate a context-aware response  

---

### 6️⃣ Change the Wikipedia Topic (Optional)

To use a different Wikipedia topic, open `.env_example` (or `.env`) and edit:

```bash
WIKIPEDIA_TOPIC="Machine Learning"
```

Then rerun:
```bash
python src/app.py
```

---

### 7️⃣ Adjust Chunk Settings (Optional)

You can fine-tune performance and accuracy by changing these in `.env_example`:

```bash
CHUNK_SIZE=800
CHUNK_OVERLAP=150
```

Larger chunks give more context per query, but smaller chunks may improve retrieval precision.

---

### 8️⃣ Ask Your Own Questions 🔍

After setup, modify the query inside `rag.py` or extend the app to accept input dynamically.

For example, in `rag.py`:
```python
query = "Who are the pioneers of Artificial Intelligence?"
```

You can also build a simple interactive mode:
```python
question = input("Ask your question: ")
answer = rag_response(question, embeddings)
print(answer)
```

Now you can ask Gemini your own questions using real Wikipedia knowledge.

---

## 🗂️ Folder Structure

```
RAG-Wikipedia-Assitant/
├── src/
│   ├── scraper/
│   │   └── scraper.py          # Wikipedia text scraper
│   ├── rag_chain/
│   │   └── rag.py              # RAG pipeline (Gemini + FAISS)
│   ├── app.py                  # Main entry point (auto .env setup)
│
├── wikipedia_pages/            # Saved Wikipedia text files
├── vectorstore/                # FAISS vector index files
├── .env                        # Default environment variables
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignored files
└── README.md                   # Documentation
```

---

## 🔄 RAG Workflow

1. 🧑‍💻 User asks a question  
2. 🌍 Scraper retrieves relevant Wikipedia text  
3. ✂️ Text is split into chunks  
4. 🧠 FAISS indexes embeddings  
5. 🔍 Retriever finds relevant context  
6. 💬 Gemini generates the final answer  

---

## 👥 Authors

| Name | Role |
|------|------|
| **Ramadan** | GitHub & Documentation |
| **Manas** | Wikipedia Scraper |
| **Mohammad Anas** | RAG Chain Development |
| **Akinpeumi** | Integrations & Testing |

---

## 💡 Notes

- 🧩 `.env_example` is auto-created if missing.  
- ⚙️ Works with both `python src/app.py` and `python -m src.app`.  
- 🧠 Uses **LangChain + FAISS + Gemini** for reliable RAG-based QA.  

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project with attribution.

---

### ⭐ Star this repository if you found it helpful!
