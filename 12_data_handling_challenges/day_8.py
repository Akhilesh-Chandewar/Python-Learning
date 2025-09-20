import json
import os
from typing import Any, Dict, List, Union

INPUT_FILE = "day_8_nested.json"
OUTPUT_FILE = "day_8_flatten.json"


def load_json_data(filename: str) -> Union[List[Any], Dict[str, Any]]:
    """Load JSON data from file, return [] if not found or invalid."""
    if not os.path.exists(filename):
        print(f"❌ File '{filename}' not found.")
        return []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print(f"❌ Error decoding JSON data from '{filename}'.")
        return []


def flatten_json(data: Any, parent_key: str = "", sep: str = ".") -> Dict[str, Any]:
    """Recursively flatten a nested JSON object."""
    items: Dict[str, Any] = {}
    if isinstance(data, dict):
        for key, value in data.items():
            new_key = f"{parent_key}{sep}{key}" if parent_key else key
            items.update(flatten_json(value, new_key, sep=sep))
    elif isinstance(data, list):
        for i, item in enumerate(data):
            new_key = f"{parent_key}[{i}]" if parent_key else f"[{i}]"
            items.update(flatten_json(item, new_key, sep=sep))
    else:
        items[parent_key] = data
    return items


def save_json_data(data: Any, filename: str) -> None:
    """Save JSON data to file."""
    if not data:
        print("⚠️ No data to save.")
        return

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    print(f"✅ JSON file saved as '{filename}'")


if __name__ == "__main__":
    data = load_json_data(INPUT_FILE)

    if isinstance(data, list):
        flattened = [flatten_json(item) for item in data]
    else:
        flattened = flatten_json(data)

    save_json_data(flattened, OUTPUT_FILE)

    print(f"✅ JSON file saved as '{OUTPUT_FILE}'")