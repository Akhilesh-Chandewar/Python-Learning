import string
import random
import getpass


def check_password_strength(password: str) -> tuple[bool, list[str]]:
    issues: list[str] = []

    if len(password) < 8:
        issues.append("Password should be at least 8 characters long.")

    if not any(char.isupper() for char in password):
        issues.append("Password should contain at least one uppercase letter.")

    if not any(char.islower() for char in password):
        issues.append("Password should contain at least one lowercase letter.")

    if not any(char.isdigit() for char in password):
        issues.append("Password should contain at least one digit.")

    if not any(char in string.punctuation for char in password):
        issues.append("Password should contain at least one special character.")

    if issues:
        return False, issues
    else:
        return True, issues


def generate_password(length: int = 12) -> str:
    if length < 8:
        raise ValueError("Password length should be at least 8 characters.")
    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(random.choice(characters) for _ in range(length))


def get_password() -> str:
    return getpass.getpass("Enter your password: ")


if __name__ == "__main__":
    password = get_password()
    is_strong, issues = check_password_strength(password)
    if is_strong:
        print("✅ Password is strong!")
    else:
        print("⚠️ Password is weak. Here are some suggestions:")
        for issue in issues:
            print(f"- {issue}")
        print("\n💡 Suggested strong password:", generate_password())

    print("\nGoodbye!")