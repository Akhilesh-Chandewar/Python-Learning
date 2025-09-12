snack = input("Enter your preffered snack! ")
snack = snack.lower().strip()

if snack == "cookie" or snack == "samosa":
    print(f"Great choice! We will sever you {snack}")
else:
    print(f"Sorry! We are out of {snack}")
