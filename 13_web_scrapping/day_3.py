import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin
from typing import List, Dict, Tuple, Optional

BASE_URL = "https://books.toscrape.com/"
START_PAGE = "catalogue/page-1.html"
OUTPUT_PAGE = "day_3_books_data.json"
TARGET_COUNT = 70


def scrape_page(url: str) -> Tuple[List[Dict[str, str]], Optional[str]]:
    """
    Scrape a single page of books and return the books data with next page URL (if exists).
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return [], None

    soup = BeautifulSoup(response.text, "html.parser")

    books: List[Dict[str, str]] = []
    for article in soup.select("article.product_pod"):
        title_tag = article.select_one("h3 > a")
        price_tag = article.select_one(".price_color")

        if not title_tag or not price_tag:
            continue

        title = str(title_tag["title"])
        price = price_tag.get_text(strip=True)
        link = urljoin(url, str(title_tag["href"]))  # ✅ cast to str

        book = {
            "title": title,
            "price": price,
            "link": link,
        }
        books.append(book)

    # find next page link
    next_page_tag = soup.select_one("li.next > a")
    next_page_url = (
        urljoin(url, str(next_page_tag["href"])) if next_page_tag else None
    )  # ✅ cast to str

    return books, next_page_url


def main() -> None:
    """
    Scrape books across multiple pages until TARGET_COUNT is reached or pages end.
    Save results to OUTPUT_PAGE.
    """
    collected: List[Dict[str, str]] = []
    current_url: Optional[str] = urljoin(BASE_URL, START_PAGE)

    while len(collected) < TARGET_COUNT and current_url:
        books, next_url = scrape_page(current_url)
        collected.extend(books)

        if not next_url:
            break
        current_url = next_url

    # trim to target count if needed
    collected = collected[:TARGET_COUNT]

    with open(OUTPUT_PAGE, "w", encoding="utf-8") as file:
        json.dump(collected, file, indent=4, ensure_ascii=False)

    print(f"✅ Saved {len(collected)} books to {OUTPUT_PAGE}")


if __name__ == "__main__":
    main()
