class InvalidChaiError(Exception):
    pass


def bill(flavour, cups):
    menu = {"masala": 20, "ginger": 10}
    try:
        if flavour not in menu:
            raise InvalidChaiError(f"Unknown chai {flavour}")

        if not isinstance(cups, (int, float)):
            raise TypeError("Cups must be a number")

        total = menu[flavour] * cups
        print(f"Your bill for {cups} cups of {flavour} chai is {total}")

    except InvalidChaiError as e:
        print("Error:", e)
    except TypeError as e:
        print("Error:", e)
    except Exception as e:
        print("Unexpected Error:", e)
    finally:
        print("Order processing completed")

bill("ginger", 2)  # valid case
bill("masala", 3)  # valid case
bill("elaichi", 2)  # invalid flavour
bill("masala", "two")  # invalid cups
bill("masala", -1)  # valid technically, but negative cups
