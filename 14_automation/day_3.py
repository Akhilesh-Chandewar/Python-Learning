import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

WATCH_FOLDER = "watch_folder"
DESTINATION_FOLDER = "destination_folder"

FILE_DEST = {
    ".pdf": "PDFS",
    ".jpg": "IMAGES",
    ".jpeg": "IMAGES",
    ".png": "IMAGES",
    ".txt": "TEXT",
}


def move_file(src_path):
    if not os.path.isfile(src_path):  # skip directories
        return

    _, ext = os.path.splitext(src_path)
    ext = ext.lower()

    # choose destination subfolder
    folder_name = FILE_DEST.get(ext, "OTHERS")
    dest_folder = os.path.join(DESTINATION_FOLDER, folder_name)

    # create folder if missing
    os.makedirs(dest_folder, exist_ok=True)

    # build destination path
    filename = os.path.basename(src_path)
    dest_path = os.path.join(dest_folder, filename)

    try:
        shutil.move(src_path, dest_path)
        print(f"Moved {filename} → {dest_folder}")
    except Exception as e:
        print(f"❌ Failed to move {filename}: {e}")


class MoveFilesHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            print(f"📂 File created: {event.src_path}")
            move_file(event.src_path)

    def on_modified(self, event):
        if not event.is_directory:
            print(f"✏️ File modified: {event.src_path}")
            move_file(event.src_path)

    def on_deleted(self, event):
        if not event.is_directory:
            print(f"🗑️ File deleted: {event.src_path}")


if __name__ == "__main__":
    os.makedirs(WATCH_FOLDER, exist_ok=True)
    os.makedirs(DESTINATION_FOLDER, exist_ok=True)

    event_handler = MoveFilesHandler()
    observer = Observer()
    observer.schedule(event_handler, WATCH_FOLDER, recursive=False)

    observer.start()
    print(f"👀 Watching folder: {WATCH_FOLDER}")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
