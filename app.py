from scraper.scraper import scrape_page
from rag.rag_chain import rag_response

def main():
    print("=== RAG Wikipedia Assistant ===")
    query = input("Enter your question: ")
    
    # For now, show scraper output only
    scraped_text = scrape_page(query)
    print("\n[SCRAPED WIKIPEDIA CONTENT PREVIEW]\n")
    print(scraped_text[:800])  # print only start of content
    
    # Placeholder RAG answer
    print("\n[RAG ANSWER]\n")
    print(rag_response(query))

if __name__ == "__main__":
    main()
