# 🧠 RAG Wikipedia Assistant

A **Retrieval-Augmented Generation (RAG)** system that answers questions using real **Wikipedia knowledge** rather than relying only on an LLM’s internal memory.

It combines:
-  Wikipedia Scraping  
-  Text Chunking  
-  Embedding & Vector Search (FAISS)  
-  Context-Aware Answer Generation via LangChain  

---

##  Project Goal
Provide fact-based, verifiable answers by retrieving relevant Wikipedia text before generating a response — reducing hallucinations and improving accuracy.

---

##  Setup Instructions

```bash
# 1. Clone the repository
git clone https://github.com/Ramee4sure/RAG-Wikipedia-Assitant.git
cd RAG-Wikipedia-Assitant

# 2. Create a virtual environment (optional but recommended)
python -m venv venv
venv\Scripts\activate   # On Windows
source venv/bin/activate  # On Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Copy .env_example to .env and fill in your API keys
cp .env_example .env
python src/app.py
The assistant will:

1.Scrape a Wikipedia topic

2.Build a FAISS vector store

3.Retrieve the most relevant context

4.Generate a context-aware response

FOLDER STRUCTURE
RAG-Wikipedia-Assitant/
├── src/
│   ├── scraper/
│   │   └── scraper.py          # Wikipedia text scraper
│   ├── rag/
│   │   └── rag_chain.py        # RAG pipeline
│   ├── app.py                  # Demo runner
│
├── .env_example                # Template for environment variables
├── requirements.txt            # Project dependencies
├── .gitignore                  # Ignore sensitive/system files
└── README.md                   # Documentation
python src/app.py


🔄 RAG Workflow

1.User asks a question

2.Scraper retrieves relevant Wikipedia text

3.Embeddings are generated from the text

4.Vector Database (FAISS) stores & indexes chunks

5.Retriever finds the most relevant context

6.LLM generates the final answer using that context

👥 Authors

Ramadan — GitHub & Documentation

Team Member 2 — Wikipedia Scraper

Team Member 3 — RAG Chain Development

Team Member 4 — Documentation & Integrations