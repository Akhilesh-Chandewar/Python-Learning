chai_prices = {
    "small" : 10,
    "medium" : 15,
    "large" : 20
}

price = input("Enter the size of chai: ")
price = price.lower().strip()

if price in chai_prices:
    print(f"Chai price is {chai_prices[price]}")
else:
    print("Unknown cup size")