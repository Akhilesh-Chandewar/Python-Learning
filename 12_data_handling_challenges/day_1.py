import csv
import os
from typing import Dict, List

FILE_NAME = "day_1_contacts.csv"

# Ensure file exists with headers
if not os.path.exists(FILE_NAME):
    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Name", "Phone", "Email"])


def add_contact():
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()

    if not name or not phone or not email:
        print("All fields are required!")
        return

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print("Name already exists")
                return

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([name, phone, email])

    print("Contact added.")


def list_contacts():
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        contacts = list(reader)
        if not contacts:
            print("No contacts found.")
            return
        for row in contacts:
            print(f"{row['Name']} - {row['Phone']} - {row['Email']}")


def search_contact():
    name = input("Enter name to search: ").strip()
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                print(f"{row['Name']} - {row['Phone']} - {row['Email']}")
                return
    print("Contact not found.")


def delete_contact():
    name = input("Enter name to delete: ").strip()
    rows: List[Dict[str, str]] = []
    found = False

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() != name.lower():
                rows.append(row)
            else:
                found = True

    if not found:
        print("Contact not found.")
        return

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(rows)

    print("Contact deleted.")


def update_contact():
    name = input("Enter name to update: ").strip()
    rows: List[Dict[str, str]] = []
    found = False

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["Name"].lower() == name.lower():
                found = True
                print("Leave field blank to keep existing value.")
                new_phone = (
                    input(f"New Phone ({row['Phone']}): ").strip() or row["Phone"]
                )
                new_email = (
                    input(f"New Email ({row['Email']}): ").strip() or row["Email"]
                )
                row["Phone"] = new_phone
                row["Email"] = new_email
            rows.append(row)

    if not found:
        print("Contact not found.")
        return

    with open(FILE_NAME, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["Name", "Phone", "Email"])
        writer.writeheader()
        writer.writerows(rows)

    print("Contact updated.")


def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")

        choice = input("Choose an option (1-6): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            update_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
