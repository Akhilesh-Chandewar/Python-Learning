# file = open("order.txt" , "w")

# try:
#     file.write("Hello World")
# except Exception as e:
#     print(e)
# finally:
#     file.close()

with open("order.txt" , "w") as file:
    file.write("ginger tea - 4 cups")