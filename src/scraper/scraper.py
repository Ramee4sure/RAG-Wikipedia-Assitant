"""
Wikipedia Scraper Module
------------------------

This module provides utilities for scraping and saving
Wikipedia pages as text files for use in the RAG pipeline.

Functions:
1. scrape_page()         - Fetches a single Wikipedia page.
2. save_to_text_file()   - Saves content to a text file.
3. scrape_multiple()     - Fetches and saves multiple pages.
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import os
import logging


# ------------------------------------------------------------
# Logging Configuration
# ------------------------------------------------------------
LOG_FORMAT = "[%(asctime)s] [%(levelname)s] %(message)s"
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
logger = logging.getLogger(__name__)


# ------------------------------------------------------------
# Scrape a Single Wikipedia Page
# ------------------------------------------------------------
def scrape_page(query: str, summary_only: bool = False, lang: str = "en") -> str:
    """
    Scrapes a Wikipedia page and returns the page content or summary.

    Args:
        query (str): The title or search term for the Wikipedia page.
        summary_only (bool): If True, return only the summary of the page.
        lang (str): Language code (default is "en" for English).

    Returns:
        str: The page content, summary, or an error message.
    """
    wikipedia.set_lang(lang)
    logger.info(f"Scraping page for query: '{query}' (lang={lang})")

    try:
        search_results = wikipedia.search(query)
        if not search_results:
            msg = f"No page found for '{query}'."
            logger.warning(msg)
            return msg

        page_title = search_results[0]
        page = wikipedia.page(page_title)

        logger.info(f"Successfully fetched page: '{page_title}'")
        return page.summary if summary_only else page.content

    except DisambiguationError as e:
        msg = (
            f"Disambiguation page: '{query}' has multiple meanings. "
            f"Try one of: {', '.join(e.options[:5])}..."
        )
        logger.warning(msg)
        return msg

    except PageError:
        msg = f"No valid page found for '{query}'."
        logger.error(msg)
        return msg

    except Exception as e:
        msg = f"Error fetching '{query}': {e}"
        logger.exception(msg)
        return msg


# ------------------------------------------------------------
# Save Content to Text File
# ------------------------------------------------------------
def save_to_text_file(folder_path: str, title: str, content: str) -> None:
    """
    Saves scraped Wikipedia content to a text file.
    Automatically creates the output folder if it does not exist.

    Args:
        folder_path (str): Directory path to save the text files.
        title (str): Name of the Wikipedia page.
        content (str): Page content to write into the file.
    """
    os.makedirs(folder_path, exist_ok=True)

    # Clean up filename to remove invalid characters
    safe_title = "".join(
        c for c in title if c.isalnum() or c in (" ", "_", "-")
    ).rstrip()
    file_path = os.path.join(folder_path, f"{safe_title}.txt")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        logger.info(f"Saved: {file_path}")
    except Exception as e:
        logger.exception(f"Error saving '{title}': {e}")


# ------------------------------------------------------------
# Scrape and Save Multiple Wikipedia Pages
# ------------------------------------------------------------
def scrape_multiple(
    page_list: list, summary_only: bool = False, lang: str = "en"
) -> dict:
    """
    Scrapes multiple Wikipedia pages and saves them as text files.

    Args:
        page_list (list): A list of Wikipedia page titles.
        summary_only (bool): Whether to fetch only summaries.
        lang (str): Language code (default "en").

    Returns:
        dict: Status report containing number of pages scraped and saved.
    """
    saved = 0
    logger.info(f"Starting multi-page scrape for {len(page_list)} pages...")

    for query in page_list:
        content = scrape_page(query, summary_only, lang)

        # Skip if the content indicates an error or disambiguation
        if isinstance(content, str) and (
            content.startswith("Error")
            or content.startswith("No page found")
            or content.startswith("Disambiguation page")
            or content.startswith("No valid page")
        ):
            logger.warning(f"Skipping '{query}' due to issue: {content}")
            continue

        save_to_text_file("wikipedia_pages", query, content)
        saved += 1

    logger.info(f"Scraping completed. Saved {saved}/{len(page_list)} pages.")
    return {
        "status": "completed",
        "pages_scraped": len(page_list),
        "pages_saved": saved,
    }


# ------------------------------------------------------------
# Example Usage
# ------------------------------------------------------------
if __name__ == "__main__":
    pages = [
        "Artificial Intelligence",
        "Machine Learning",
        "Natural Language Processing",
    ]
    scrape_multiple(pages, summary_only=False, lang="en")
