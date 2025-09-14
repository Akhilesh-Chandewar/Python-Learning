def server_chai():
    chai_type = "masala chai" #local scope
    print(f"Inside fucntion {chai_type}")

chai_type = "green tea" #global scope
server_chai()
print(f"Outside fucntion {chai_type}")

def chai_counter():
    chai_order = "lemon" #enclosing
    def print_order():
        chai_order = "ginger"
        print("Inner: ", chai_order)
    print("Outer: ", chai_order)
    print_order()
    print("Outer: ", chai_order)

chai_order = "Tulsi"
chai_counter()
print("Global: ", chai_order)