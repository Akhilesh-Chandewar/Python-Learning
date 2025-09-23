import csv
import matplotlib.pyplot as plt
import datetime

CSV_FILE = "day_7_coins_data.csv"


def load_data(coin_name):
    timestamps = []
    prices = []

    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["coin"].lower() == coin_name.lower():
                timestamps.append(
                    datetime.datetime.strptime(row["timestamp"], "%Y-%m-%d %H:%M:%S")
                )
                prices.append(float(row["price (USD)"]))

    return timestamps, prices


def plot_coin(coin_name):
    timestamps, prices = load_data(coin_name)

    if not timestamps:
        print(f"No data found for {coin_name}")
        return

    plt.figure(figsize=(10, 5))
    plt.plot(
        timestamps, prices, marker="o", linestyle="-", label=coin_name, color="blue"
    )

    plt.title(f"{coin_name} Price Over Time")
    plt.xlabel("Timestamp")
    plt.ylabel("Price (USD)")
    plt.xticks(rotation=45)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend()
    plt.tight_layout()
    plt.savefig("day_7_coin_prices.png", dpi=300)


if __name__ == "__main__":
    plot_coin("Bitcoin")  # 👈 change coin name as needed
