import sqlite3
import datetime
import requests

# CoinGecko API
API_URL = "https://api.coingecko.com/api/v3/coins/markets"
PARAMS = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 5,  # top 5 coins
    "page": 1,
    "sparkline": "false",
}

# SQLite DB file
DB_FILE = "day_9_coins.db"


def init_db():
    """Create SQLite table if it doesn’t exist."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS coins (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            coin TEXT,
            price REAL
        )
    """
    )
    conn.commit()
    conn.close()


def save_to_db(coin):
    """Insert one coin’s data into DB."""
    conn = sqlite3.connect(DB_FILE)
    cur = conn.cursor()
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cur.execute(
        "INSERT INTO coins (timestamp, coin, price) VALUES (?, ?, ?)",
        (timestamp, coin["name"], coin["current_price"]),
    )
    conn.commit()
    conn.close()


def fetch_and_store():
    """Fetch data from CoinGecko and save into DB."""
    try:
        response = requests.get(API_URL, params=PARAMS, timeout=10)
        response.raise_for_status()
        coins = response.json()

        for coin in coins:
            save_to_db(coin)
            print(f"✅ Saved {coin['name']} at {coin['current_price']} USD")

    except requests.RequestException as e:
        print(f"❌ API request failed: {e}")


if __name__ == "__main__":
    init_db()
    fetch_and_store()
