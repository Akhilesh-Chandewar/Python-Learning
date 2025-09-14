def chai_flavour(falvour = "ginger"):
    """Return flavours of chai"""
    return falvour

print(chai_flavour.__name__)
print(chai_flavour.__doc__)

# help(len)

def generate_bill(chai = 0, samosa = 0):
    """
    Calculate the bill for chai and samosa
    :param chai: chai quantity
    :param samosa: samosa quantity
    :return: total bill
    """
    total = chai * 10 + samosa * 5
    return total , "Thank you for ordering chai and samosa!"

print(generate_bill.__name__)
print(generate_bill.__doc__)