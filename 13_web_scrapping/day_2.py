import csv 
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "day_2_hacker_news.csv"

def fetch_top_post():
    try:
        response = requests.get(HN_URL , timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the page: {e}")
        return []
    
    soup = BeautifulSoup(response.text , "html.parser")
    posts = soup.select("span.titleline > a")
    return posts

def write_to_csv(posts):
    if not posts:
        print("No posts found.")
        return
    with open(CSV_FILE , "w" , newline="" , encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title" , "Link"])
        for post in posts:
            title = post.get_text()
            link = post["href"]
            writer.writerow([title , link])

posts = fetch_top_post()
write_to_csv(posts)
