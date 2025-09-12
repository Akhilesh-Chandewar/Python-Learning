order_amount = int(input("Enter your order amount: "))

delivery_fee = 0 if order_amount > 300 else 30

print(f"Delivery fee is {delivery_fee}")
