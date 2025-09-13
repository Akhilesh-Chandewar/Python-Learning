flovours = [
    "vanilla",
    "chocolate",
    "out of stock",
    "strawberry",
    'discontinued'
    "raspberry",
]

for flavour in flovours:
    if flavour == "out of stock":
        continue
    if flavour == "discontinued":
        break
    
    print(f"Flavour: {flavour}")

