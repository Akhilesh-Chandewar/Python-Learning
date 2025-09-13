value = 13
reamainder = value % 5
if reamainder :
    print(f"remainder : {reamainder}")

if (reamainder := value % 5):
    print(f"remainder : {reamainder}")

available_sizes = ["small" , "medium" , "large"]
if (requested_size := input("Enter the size of chai: ")):
    if requested_size in available_sizes:
        print(f"chai size is {requested_size}")
    else:
        print("Unknown cup size")
else:
    print("No size provided")

flavours = ["masala" , "ginger" , "lemon" , "mint"]
print(f"flavours are {flavours}")

while(flavour := input("Enter the flavour of chai: ")) not in flavours:
    print(f"Unknown flavour {flavour}")
print(f"Flavour is {flavour}")