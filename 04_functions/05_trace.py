def add_vat(price , vat_rate):
    return price + (price * (vat_rate / 100))

orders = [100 , 150 , 200]

for order in orders:
    print(add_vat(order , 20))

