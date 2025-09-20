import os
import csv
from datetime import datetime
import requests

FILENAME = "day_4_weather_logs.csv"
API_KEY = "YOUR_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

# ✅ Create file with headers if it doesn't exist
if not os.path.exists(FILENAME):
    with open(FILENAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["City", "Temperature (°C)", "Humidity (%)", "Pressure (hPa)", "Date"]
        )


def log_weather():
    city = input("Enter your city: ").strip()
    if not city:
        print("❌ City name cannot be empty.")
        return

    try:
        # Request weather data
        response = requests.get(
            BASE_URL, params={"q": city, "appid": API_KEY, "units": "metric"}
        )
        response.raise_for_status()  # Raise error for bad HTTP codes
        data = response.json()

        # Handle API-level errors
        if data.get("cod") != 200:
            print(f"❌ Error: {data.get('message', 'Unknown error')}")
            return

        # Extract data safely
        temp = data["main"].get("temp", "N/A")
        humidity = data["main"].get("humidity", "N/A")
        pressure = data["main"].get("pressure", "N/A")
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Save to CSV
        with open(FILENAME, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow([city, temp, humidity, pressure, date])

        print(
            f"✅ Logged weather for {city}: {temp}°C, {humidity}% humidity, {pressure} hPa"
        )

    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
    except Exception as e:
        print(f"⚠️ Unexpected error: {e}")


def view_logs():
    if not os.path.exists(FILENAME):
        print("📂 No logs found yet.")
        return

    with open(FILENAME, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        print("\n📜 Weather Logs:")
        for row in reader:
            print(
                f"{row['Date']} | {row['City']} | {row['Temperature (°C)']}°C | "
                f"Humidity: {row['Humidity (%)']}% | Pressure: {row['Pressure (hPa)']} hPa"
            )


def main():
    while True:
        print("\n🌤️ Weather Logger")
        print("1. Log Weather")
        print("2. View Logs")
        print("3. Exit")

        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            log_weather()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice, please select 1, 2, or 3.")


if __name__ == "__main__":
    main()
