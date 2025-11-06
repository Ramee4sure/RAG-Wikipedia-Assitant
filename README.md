# RAG Wikipedia Assistant

This project is a Retrieval-Augmented Generation (RAG) system that answers questions based on Wikipedia knowledge instead of relying only on the model's built-in memory.

It combines:
- Wikipedia Scraping
- Text Chunking
- Embedding & Vector Search using FAISS
- Context-Aware Answer Generation using LangChain


# Project Goal
The system provides **fact-based responses** by retrieving information from Wikipedia before generating an answer.  
This reduces hallucinations and improves accuracy.


# Setup Instructions

# Clone the Repository
git clone https://github.com/Ramee4sure/RAG-Wikipedia-Assitant.git
cd RAG-Wikipedia-Assitant
pip install -r requirements.txt

RAG-Wikipedia-Assistant/
│
├── src/
│   ├── scraper/
│   │   └── scraper.py          # Wikipedia text scraper
│   ├── rag/
│       └── rag_chain.py        # RAG pipeline
│
├── .env_example                # Template for API keys
├── requirements.txt            # Dependencies
└── README.md                   # Documentation

