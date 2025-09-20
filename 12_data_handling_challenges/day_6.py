import json
import csv
import os

INPUT_FILE = "day_6.json"
OUTPUT_FILE = "day_6.csv"


def load_json_data(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"Error decoding JSON data from '{filename}'.")
        return []


def save_csv_data(data, filename):
    if not data:
        print("No data to save.")
        return

    # Extract headers from keys of the first dictionary
    headers = data[0].keys()

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        for entry in data:
            writer.writerow([entry.get(h, "") for h in headers])


if __name__ == "__main__":
    data = load_json_data(INPUT_FILE)
    save_csv_data(data, OUTPUT_FILE)
    print(f"CSV file saved as '{OUTPUT_FILE}'")
