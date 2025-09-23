import os
import requests
import textwrap
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw, ImageFont

BASE_URL = "https://quotes.toscrape.com/"
OUTPUT_DIR = "day_6_quotes"


def fetch_quotes():
    """Fetch top 5 quotes from the homepage."""
    response = requests.get(BASE_URL, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    quotes = soup.select("div.quote")

    quote_data = []
    for q in quotes[:5]:
        quote_text_tag = q.find("span", class_="text")
        quote_author_tag = q.find("small", class_="author")

        if not quote_text_tag or not quote_author_tag:
            continue

        quote_text = quote_text_tag.get_text(strip=True)
        quote_author = quote_author_tag.get_text(strip=True)
        quote_data.append({"text": quote_text, "author": quote_author})

    return quote_data


def create_image(text: str, author: str, index: int) -> None:
    """Create a styled image with the quote and save to file."""
    width, height = 900, 500
    background_color = "#fefcfb"  # soft white
    text_color = "#1a1a1a"  # deep gray
    accent_color = "#e07a5f"  # warm accent for author

    # Create canvas
    image = Image.new("RGB", (width, height), background_color)
    draw = ImageDraw.Draw(image)

    # Try loading a nicer font (falls back if not available)
    try:
        font = ImageFont.truetype("DejaVuSans.ttf", 28)
        author_font = ImageFont.truetype("DejaVuSans-Bold.ttf", 24)
    except Exception:
        font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Wrap quote text
    wrapped = textwrap.fill(text, width=50)

    # Center text vertically
    y_text = 120
    for line in wrapped.split("\n"):
        bbox = draw.textbbox((0, 0), line, font=font)
        w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
        x = (width - w) // 2
        draw.text((x, y_text), line, font=font, fill=text_color)
        y_text += h + 8

    # Author aligned bottom-right
    author_text = f"- {author}"
    bbox = draw.textbbox((0, 0), author_text, font=author_font)
    w, h = bbox[2] - bbox[0], bbox[3] - bbox[1]
    draw.text(
        (width - w - 40, height - h - 60),
        author_text,
        font=author_font,
        fill=accent_color,
    )

    # Save output
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    filepath = os.path.join(OUTPUT_DIR, f"quote_{index+1}.png")
    image.save(filepath)
    print(f"✅ Saved {filepath}")


def main():
    quotes = fetch_quotes()
    for i, q in enumerate(quotes):
        create_image(q["text"], q["author"], i)


if __name__ == "__main__":
    main()
