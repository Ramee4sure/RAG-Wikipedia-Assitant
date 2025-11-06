# RAG Wikipedia Assistant

This project is a Retrieval-Augmented Generation (RAG) system that answers questions using real Wikipedia knowledge, instead of relying only on the language model’s internal memory.

It combines:

-  Wikipedia Scraping  
-  Text Chunking  
-  Embedding & Vector Search (FAISS)  
-  Context-Aware Answer Generation using LangChain  


##  Project Goal
The system provides fact-based, verifiable responses by retrieving relevant Wikipedia text before generating an answer.  
This reduces hallucinations and improves accuracy.


---

##  Setup Instructions

###  Clone the Repository
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


