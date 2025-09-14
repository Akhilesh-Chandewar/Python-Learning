def make_chai():
    # return "Here id your masala chai"
    print("Here id your masala chai")
return_value = make_chai()
print(return_value)

def ideal_chaiwala():
    pass
print(ideal_chaiwala())

def sold_cups():
    return 120
total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return "chai is out of stock"
    return f"{cups_left} cups left"
print(chai_status(0))
print(chai_status(10))

def chai_report():
    return 100 , 20 , 10
sold , remaining , _ = chai_report()
print(sold)
print(remaining)