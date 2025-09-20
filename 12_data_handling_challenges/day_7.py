import json
import csv
import os

INPUT_FILE = "day_7.csv"
OUTPUT_FILE = "day_7.json"


def load_csv_data(filename):
    if not os.path.exists(filename):
        print(f"File '{filename}' not found.")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return list(csv.DictReader(f))
    except csv.Error:
        print(f"Error decoding CSV data from '{filename}'.")
        return []
    

def save_json_data(data, filename):
    if not data:
        print("No data to save.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"JSON file saved as '{filename}'")


if __name__ == "__main__":
    data = load_csv_data(INPUT_FILE)
    save_json_data(data, OUTPUT_FILE)