import textwrap

name = input("What is your name? ").strip()
profession = input("What is your profession? ").strip()
passion = input("Enter your passion in one line: ").strip()
emoji = input("Enter your favorite emoji: ").strip()
website = input("Enter your website: ").strip()

print("\nChoose your style: ")
print("1 : Simple line ")
print("2 : Vertical flair")
print("3 : Emoji sandwich")

style = input("Enter 1 ,2 or 3: ").strip()


def generate_bio(style):
    if style == "1":
        return f"{emoji} {name} | {profession}\n{passion}\n{website}"

    elif style == "2":
        return f"{emoji} {name}\n{profession} 🔥\n{passion}\n{website} 🔥"

    elif style == "3":
        return f"{emoji * 3}\n{name} - {profession}\n{passion}\n{website}\n{emoji * 3}"

    else:
        return "Invalid choice."


bio = generate_bio(style)

print("\nYour stylish bio")
print("*" * 80)
print(bio)
print("*" * 80)

save = input("Do you want to save this bio? (y/n): ").strip().lower()
if save == "y":
    file_name = f"{name.lower().replace(' ', '_')}_bio.txt"
    with open(file_name, "w", encoding="utf-8") as f:
        f.write(bio)
    print(f"File saved as {file_name}")
