def brew_chai(flavour):
    if flavour not in ["masala" , "ginger" , "lemon" , "mint"]:
        raise ValueError(f"Unknown flavour {flavour}")
    print(f"Brewing chai for {flavour}")

try:
    brew_chai("black")
except ValueError as e:
    print(e)