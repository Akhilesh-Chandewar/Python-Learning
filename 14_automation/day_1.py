import os
import shutil

EXTENSION_MAP = {
    "PDFS": [".pdf"],
    "IMAGES": [".jpg", ".jpeg", ".png"],
    "TEXT": [".txt"],
}


def get_destination_folder(filename: str) -> str:
    ext = os.path.splitext(filename)[1].lower()
    for folder, extensions in EXTENSION_MAP.items():
        if ext in extensions:
            return folder
    return "OTHERS"


def sort_files():
    # create folders if not exist
    for folder in list(EXTENSION_MAP.keys()) + ["OTHERS"]:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # move files
    for filename in os.listdir():
        if os.path.isfile(filename) and not filename.endswith(".py"):
            folder = get_destination_folder(filename)
            dest_path = os.path.join(folder, filename)
            print(f"Moving {filename} → {dest_path}")
            shutil.move(filename, dest_path)


if __name__ == "__main__":
    sort_files()
