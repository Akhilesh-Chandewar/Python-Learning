even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

daily_sales = [1000, 500, 600, 700, 800, 900 , 1000 ]
total_cups = sum(sale for sale in daily_sales if sale > 500)
print(total_cups)
