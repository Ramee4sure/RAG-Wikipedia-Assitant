import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import os


def scrape_page(query: str, summary_only: bool = False, lang: str = "en") -> str:
    """
    Scrapes a Wikipedia page and returns the page content or summary.
    Handles disambiguation and missing page errors.
    """
    wikipedia.set_lang(lang)

    try:
        search_results = wikipedia.search(query)
        if not search_results:
            return f"No page found for '{query}'."

        page_title = search_results[0]
        page = wikipedia.page(page_title)

        return page.summary if summary_only else page.content

    except DisambiguationError as e:
        return f"Disambiguation page: '{query}' has multiple meanings. Try one of: {', '.join(e.options[:5])}..."
    except PageError:
        return (f"No valid page found for '{query}'.",)
    except Exception as e:
        return f"Error fetching '{query}': {e}"


def save_to_text_file(folder_path: str, title: str, content: str) -> None:
    """
    Saves the scraped content from Wikipedia to a text file.
    Creates folders if they do not exist.
    """

    os.makedirs(folder_path, exist_ok=True)

    safe_title = "".join(
        c for c in title if c.isalnum() or c in (" ", "_", "-")
    ).rstrip()
    file_path = os.path.join(folder_path, f"{safe_title}.txt")

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Saved: {file_path}")
    except Exception as e:
        print(f"Error saving '{title}': {e}")


def scrape_multiple(
    page_list: list, summary_only: bool = False, lang: str = "en"
) -> dict:
    """
    Scrapes multiple Wikipedia pages and saves each of them to text files in project directory.
    """
    saved = 0
    for query in page_list:
        content = scrape_page(query, summary_only, lang)

        # FIX: make sure we log before continuing; also guard with isinstance
        if isinstance(content, str) and (
            content.startswith("Error")
            or content.startswith("No page found")
            or content.startswith("Disambiguation page")
            or content.startswith("No valid page")
        ):
            print("Skipping save due to issue:", content)
            continue

        save_to_text_file("wikipedia_pages", query, content)
        saved += 1

    return {
        "status": "completed",
        "pages_scraped": len(page_list),
        "pages_saved": saved,
    }


if __name__ == "__main__":
    # Example usage
    pages = [
        "Artificial Intelligence",
        "Machine Learning",
        "Natural Language Processing",
    ]
    scrape_multiple(pages, summary_only=False, lang="en")
