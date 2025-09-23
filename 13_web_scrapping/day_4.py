import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGES_DIR = "day_4_images"


def sanitize_filename(filename: str) -> str:
    """Replace invalid characters to create a safe filename."""
    return re.sub(r"[^\w\-.]", "_", filename).replace(" ", "_")


def download_image(img_url: str, filename: str) -> None:
    """Download an image from img_url and save to filename."""
    try:
        response = requests.get(img_url, stream=True, timeout=10)
        response.raise_for_status()
        with open(filename, "wb") as file:
            for chunk in response.iter_content(chunk_size=1024):  # ✅ fixed typo
                file.write(chunk)
        print(f"✅ Saved {filename}")
    except Exception as e:
        print(f"❌ Failed to download {filename}: {e}")


def scrape_page() -> None:
    """Scrape first 10 book images from the homepage and save locally."""
    try:
        response = requests.get(BASE_URL, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return

    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGES_DIR):
        os.makedirs(IMAGES_DIR)

    for book in books:
        title_tag = book.select_one("h3 > a")
        img_tag = book.select_one("img")

        if not title_tag or not img_tag:
            continue

        title = str(title_tag.get("title"))
        img_src = str(img_tag.get("src"))
        img_url = urljoin(BASE_URL, img_src)

        safe_filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGES_DIR, safe_filename)

        download_image(img_url, filepath)


if __name__ == "__main__":
    scrape_page()
