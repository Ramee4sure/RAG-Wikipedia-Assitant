"""
RAG Pipeline Placeholder

This file will contain:
1. Loading embeddings
2. Creating / Loading vector database
3. Retrieval step
4. Response generation step
"""

import sys
import os

##Goes up two levels of projects directory to import scraper module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from src.src.scraper.scraper import scrape_multiple


def generate_wikipedia_data(page_list: list):
    """
    Uses the scraper module to fetch and save Wikipedia pages.
    """
    page_list = []

    scrape_multiple(page_list, summary_only=False, lang="en")


generate_wikipedia_data(["Artificial Intelligence"])


def rag_response(query: str):
    """
    Temporary placeholder function.
    The RAG guy will implement this.
    """
    return "RAG system not configured yet."
