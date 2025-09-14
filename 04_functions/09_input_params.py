chai = "Ginger chai"

def prepare_chai(order):
    print("preparing" , order)

prepare_chai(chai)
print(chai)


chai = [1,2,3]

def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)
print(chai)

def make_chai(tea , milk, sugar):
    print(f"chai with {tea} , {milk} and {sugar} sugar")

make_chai("ginger tea" , "milk" , 2) #positional arguments
make_chai(tea = "ginger tea" , milk = "milk" , sugar = 2) #keyword arguments

def special_chai(*ingredients , **extras):
    print(f"Ingredients {ingredients}")
    print(f"Extras {extras}")

special_chai("Cinnamon" , "Cardamom" , "ginger" , "clove" , "black pepper" , size = "large" , sugar = 2)

def chai_orders(order=[]):
    order.append("ginger")
    return order

print(chai_orders())
print(chai_orders())
print(chai_orders())

def chai_orders(order=None):
    if order is None:
        order = []
    order.append("ginger")
    return order

print(chai_orders())
print(chai_orders())
print(chai_orders())
