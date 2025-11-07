"""
RAG Wikipedia Assistant using Gemini (langchain-google-genai)
-------------------------------------------------------------
"""

import sys
import os
import dotenv
import logging
from langchain_community.document_loaders.text import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.messages import HumanMessage

# ------------------------------------------------------------
# Fix import path for scraper (no __init__.py needed)
# ------------------------------------------------------------
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from scraper.scraper import scrape_multiple


# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# Wikipedia Scraper
# ------------------------------------------------------------
def generate_wikipedia_data(page_list: list):
    """Fetches and saves Wikipedia pages using the scraper module."""
    logger.info(f"Starting Wikipedia data generation for: {page_list}")
    scrape_multiple(page_list, summary_only=False, lang="en")
    logger.info("✅ Wikipedia data generation completed.")


# ------------------------------------------------------------
# Document Loading and Splitting
# ------------------------------------------------------------
def load_and_split_document(topic: str, chunk_size: int, chunk_overlap: int):
    """Loads a Wikipedia text file and splits it into overlapping chunks."""
    doc_path = f"wikipedia_pages/{topic}.txt"
    if not os.path.exists(doc_path):
        logger.error(f"❌ Wikipedia page not found at {doc_path}")
        raise FileNotFoundError(f"Wikipedia page not found: {doc_path}")

    doc = TextLoader(doc_path, encoding="utf-8")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        add_start_index=True,
    )

    split_docs = text_splitter.split_documents(doc.load())
    logger.info(f"📘 Document '{topic}' split into {len(split_docs)} chunks.")
    return split_docs


# ------------------------------------------------------------
# Embedding and FAISS Vector Store
# ------------------------------------------------------------
def embed_store_document(split_docs, save_path: str = "vectorstore"):
    """Embeds text chunks using Gemini embeddings and stores them in a FAISS index."""
    logger.info("Generating embeddings and creating FAISS vector store...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    vector_store = FAISS.from_documents(split_docs, embedding=embeddings)
    vector_store.save_local(save_path)

    logger.info(f"💾 Vector store saved locally at: {save_path}")
    return embeddings


# ------------------------------------------------------------
# RAG Response (Retrieval + Generation)
# ------------------------------------------------------------
def rag_response(query: str, embeddings, k: int = 3):
    """Retrieves relevant chunks from FAISS and generates a Gemini-based response."""
    logger.info(f"Performing retrieval and generating response for query: '{query}'")

    vector_store = FAISS.load_local(
        "vectorstore", embeddings=embeddings, allow_dangerous_deserialization=True
    )

    results = vector_store.similarity_search(query, k=k)
    retrieved_text = "\n\n".join([doc.page_content for doc in results])

    chat_model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", temperature=0.6)

    context_prompt = f"""
    You are a knowledgeable AI assistant.
    Use the context below to answer the question accurately and clearly.

    Context:
    {retrieved_text}

    Question:
    {query}

    Answer:
    """

    try:
        response = chat_model.invoke([HumanMessage(content=context_prompt)])
        logger.info("✅ Gemini successfully generated a response.")
        return response.content
    except Exception as e:
        logger.exception(f"Error generating Gemini response: {e}")
        return f"Error generating response: {e}"


# ------------------------------------------------------------
# Main Function (Used by app.py)
# ------------------------------------------------------------
def start_bot():
    """Main RAG pipeline function."""
    logger.info("🚀 Starting RAG Wikipedia Assistant...")

    dotenv.load_dotenv(".env_example")

    google_api_key = os.getenv("GOOGLE_API_KEY")
    topic = os.getenv("WIKIPEDIA_TOPIC", "Artificial Intelligence")
    chunk_size = int(os.getenv("CHUNK_SIZE", 500))
    chunk_overlap = int(os.getenv("CHUNK_OVERLAP", 100))

    if not google_api_key:
        logger.error("❌ Missing GOOGLE_API_KEY in .env_example")
        raise ValueError("GOOGLE_API_KEY not found in .env_example")

    logger.info("✅ Environment variables loaded successfully.")
    logger.info(f"🌐 Topic: {topic}")
    logger.info(f"🧩 Chunk size: {chunk_size}, Overlap: {chunk_overlap}")

    generate_wikipedia_data([topic])
    split_docs = load_and_split_document(topic, chunk_size, chunk_overlap)
    embeddings = embed_store_document(split_docs)

    query = "What are the main goals of Artificial Intelligence?"
    logger.info(f"🤖 Running query: {query}")

    answer = rag_response(query, embeddings)
    logger.info("💬 Gemini Answer:")
    print("\n" + answer)
