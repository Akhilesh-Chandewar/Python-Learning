import os


def batch_rename(folder, base_name, extension):
    # Ensure extension starts with dot
    if not extension.startswith("."):
        extension = "." + extension

    files = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]

    for i, filename in enumerate(files, start=1):
        new_name = f"{base_name}_{i}{extension}"
        src = os.path.join(folder, filename)
        dst = os.path.join(folder, new_name)
        os.rename(src, dst)
        print(f"Renamed: {filename} → {new_name}")


if __name__ == "__main__":
    folder = (
        input("Enter folder path or leave blank for current folder: ").strip()
        or os.getcwd()
    )

    if not os.path.isdir(folder):
        print(f"Invalid folder path: {folder}")
    else:
        base_name = input("Enter base name: ").strip()
        extension = input("Enter extension (e.g. txt, jpg): ").strip()
        batch_rename(folder, base_name, extension)
