def process_order(item, quantity):
    try:
        price = {"Masala": 20}[item]

        if not isinstance(quantity, (int, float)):
            raise TypeError("Quantity must be a number")

        cost = price * quantity
        print(f"Cost of {quantity} {item} is {cost}")

    except KeyError:
        print(f"Unknown item {item}")
    except TypeError as e:
        print(e)
    else:
        print("Order processed successfully")
    finally:
        print("Order processing completed")


process_order("Masala", 2) 
process_order(2, "Masala") 
process_order("Masala", "two")
