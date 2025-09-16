chai_menu = {"masala" : 30 , "ginger" : 20}

try:
    print(chai_menu["cinnamon"])
except KeyError:
    print(" key does not available")
