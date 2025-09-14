def calculate_bills(cups , price_per_cup):
    total = cups * price_per_cup
    return total

total = calculate_bills(10 , 2)
print(f"Total bill is {total}")