import json
import os
from cryptography.fernet import Fernet
from datetime import datetime

VAULT_FILE = "day_10_notes_vault.json"
KEY_FILE = "day_10_vault.key"


def load_or_create_key():
    """Load existing Fernet key or create a new one."""
    if not os.path.exists(KEY_FILE):
        key = Fernet.generate_key()
        with open(KEY_FILE, "wb") as f:
            f.write(key)
    else:
        with open(KEY_FILE, "rb") as f:
            key = f.read()
    return Fernet(key)


fernet = load_or_create_key()


def load_vault():
    """Load and decrypt vault data."""
    if not os.path.exists(VAULT_FILE):
        return {}

    try:
        with open(VAULT_FILE, "rb") as f:  # read as bytes
            encrypted_data = f.read()
        if not encrypted_data:
            return {}

        decrypted_data = fernet.decrypt(encrypted_data).decode("utf-8")
        return json.loads(decrypted_data)
    except Exception as e:
        print(f"⚠️ Error loading vault: {e}")
        return {}


def save_vault(data):
    """Encrypt and save vault data."""
    try:
        json_data = json.dumps(data, indent=4)
        encrypted_data = fernet.encrypt(json_data.encode("utf-8"))

        with open(VAULT_FILE, "wb") as f:  # write as bytes
            f.write(encrypted_data)

        print(f"✅ Vault saved at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    except Exception as e:
        print(f"❌ Error saving vault: {e}")


def add_note():
    """Add a new note to the vault."""
    title = input("📝 Enter note title: ").strip()
    content = input("📖 Enter note content: ").strip()

    vault = load_vault()
    vault[title] = {
        "content": content,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    }
    save_vault(vault)


def view_notes():
    """View all notes in the vault."""
    vault = load_vault()
    if not vault:
        print("📂 Vault is empty.")
        return

    print("\n=== 🔐 Your Notes ===")
    for i, (title, note) in enumerate(vault.items(), start=1):
        print(f"{i}. {title} ({note['created_at']})")
        print(f"   ➡ {note['content']}")
    print("=====================\n")


def delete_note():
    """Delete a note by title."""
    vault = load_vault()
    if not vault:
        print("📂 Vault is empty.")
        return

    title = input("❌ Enter the title of the note to delete: ").strip()
    if title in vault:
        del vault[title]
        save_vault(vault)
        print(f"🗑️ Note '{title}' deleted.")
    else:
        print(f"⚠️ Note '{title}' not found.")


def main():
    while True:
        print("\n🔒 Encrypted Notes Vault")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")

        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("👋 Exiting. Stay safe!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
