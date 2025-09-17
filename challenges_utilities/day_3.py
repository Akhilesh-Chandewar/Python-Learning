try:
    people = int(input("How many people are there in the group? "))
    if people <= 0:
        raise ValueError("Number of people must be greater than 0.")

    names = []
    for i in range(people):
        name = input(f"Enter name of person {i+1}: ").strip()
        if not name:
            raise ValueError("Name cannot be empty.")
        names.append(name)

    amount = float(input("Enter the total amount: "))
    if amount <= 0:
        raise ValueError("Amount must be greater than 0.")

    total = round(amount / people, 2)

    print("\n--- Split Bill ---")
    for i in range(people):
        print(f"{names[i]} owes: {total}")

except ValueError as e:
    print(f"Input Error: {e}")
except Exception as e:
    print(f"Something went wrong: {e}")
