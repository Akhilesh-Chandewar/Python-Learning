import csv
from collections import defaultdict
import matplotlib

matplotlib.use("Agg")  # Use non-interactive backend
import matplotlib.pyplot as plt

FILENAME = "day_4_weather_logs.csv"


def visualize_weather():
    """Visualize temperature over time from CSV file."""
    dates: list[str] = []
    temps: list[float] = []
    temp_count: defaultdict[float, int] = defaultdict(int)

    # Read CSV data
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    temp = float(row["Temperature (°C)"])
                    temps.append(temp)
                    dates.append(row["Date"])
                    temp_count[temp] += 1
                except ValueError:
                    print(f"Skipping invalid temperature: {row['Temperature (°C)']}")
    except FileNotFoundError:
        print(f"File '{FILENAME}' not found!")
        return

    if not dates:
        print("No valid data to plot.")
        return

    # Plot temperature over time
    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker="o", linestyle="-", color="tab:blue")
    plt.xlabel("Date")
    plt.ylabel("Temperature (°C)")
    plt.title("Temperature Over Time")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    # Save figure
    output_file = "day_5_temperature_plot.png"
    plt.savefig(output_file)
    print(f"✅ Plot saved as '{output_file}'")


if __name__ == "__main__":
    visualize_weather()
