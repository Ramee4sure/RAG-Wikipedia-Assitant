import wikipedia

def scrape_page(query: str) -> str:
    """
    Scrapes a Wikipedia page and returns only the page content.
    """
    try:
        search_results = wikipedia.search(query)
        if not search_results:
            return "No page found for this query."

        page = wikipedia.page(search_results[0])
        return page.content

    except Exception as e:
        return f"Error: {e}"


def scrape_multiple(page_list: list) -> dict:
    """
    Scrapes multiple Wikipedia pages and returns a dictionary:
    { "title": "content", ... }
    """
    data = {}
    for p in page_list:
        data[p] = scrape_page(p)
    return data
