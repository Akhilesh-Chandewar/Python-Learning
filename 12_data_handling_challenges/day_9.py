import base64
import os

VAULT_FILE = "day_9_vault.txt"


def _encode(text: str) -> str:
    """Encode text to Base64."""
    return base64.b64encode(text.encode("utf-8")).decode("utf-8")


def _decode(text: str) -> str:
    """Decode Base64 back to text."""
    return base64.b64decode(text.encode("utf-8")).decode("utf-8")


def password_strength(password: str) -> str:
    """Check strength of password and return label."""
    length = len(password)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score = sum([length >= 8, has_upper, has_lower, has_digit, has_special])

    labels = ["very weak", "weak", "medium", "strong", "very strong"]
    return labels[min(score, len(labels) - 1)]


def add_credential() -> None:
    website = input("Enter website: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    strength = password_strength(password)
    print(f"🔐 Password strength: {strength}")

    line = f"{website} || {username} || {password}"
    encoded_line = _encode(line)

    with open(VAULT_FILE, "a", encoding="utf-8") as f:
        f.write(f"{encoded_line}\n")

    print("✅ Credential added.")


def view_credentials() -> None:
    if not os.path.exists(VAULT_FILE):
        print("⚠️ No credentials stored yet.")
        return

    with open(VAULT_FILE, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        print("⚠️ Vault is empty.")
        return

    print("\n🔓 Stored Credentials:")
    for line in lines:
        decoded_line = _decode(line.strip())
        print(decoded_line)


if __name__ == "__main__":
    while True:
        print("\n🔑 Password Vault")
        print("1. Add Credential")
        print("2. View Credentials")
        print("3. Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_credential()
        elif choice == "2":
            view_credentials()
        elif choice == "3":
            print("👋 Exiting vault.")
            break
        else:
            print("❌ Invalid choice, please try again.")
