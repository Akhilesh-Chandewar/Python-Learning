class Chai:
    origin = "India"

print(Chai.origin)

Chai.is_hot = "True"
print(Chai.is_hot)

#creating object from class
masala = Chai()
print(f"Masaka chai origin {masala.origin}") #masala.origin
print(f"Masaka chai is hot {masala.is_hot}") #masala.is_hot

masala.is_hot = "False"
print(f"Class chai is hot {Chai.is_hot}")
print(f"Masaka chai is hot {masala.is_hot}") #masala.is_hot

masala.flavour = "masala"
print(f"Masaka chai flavour {masala.flavour}")
# print(f"Class chai flavour {Chai.flavour}")