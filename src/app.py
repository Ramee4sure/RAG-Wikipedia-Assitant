"""
Demo script for RAG Wikipedia Assistant
"""

import os
from dotenv import load_dotenv
from src.scraper.scraper import scrape_wikipedia_topic  # Make sure scraper.py exists
from src.rag.rag_chain import create_rag_chain  # Make sure rag_chain.py exists

load_dotenv()  # Load environment variables

def main():
    print("🚀 Starting RAG Wikipedia Assistant Demo...\n")

    # Step 1: Scrape Wikipedia
    topic = "Haile Gebrselassie"
    print(f"📘 Scraping Wikipedia for topic: {topic}")
    results = scrape_wikipedia_topic(topic)
    if not results:
        print("❌ Failed to scrape Wikipedia.")
        return
    
    content = results[0]["content"]
    print("✅ Scraping complete. Content length:", len(content))

    # Step 2: Build RAG Chain
    print("\n⚙️  Building RAG Chain...")
    rag_chain = create_rag_chain(content)

    # Step 3: Run a sample query
    question = "What are the achievements of Haile Gebrselassie?"
    print(f"\n🧩 Query: {question}")
    response = rag_chain.invoke({"question": question})
    print("\n💬 Response:\n", response)

if __name__ == "__main__":
    main()
