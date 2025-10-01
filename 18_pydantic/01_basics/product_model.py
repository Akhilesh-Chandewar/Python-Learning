from pydantic import BaseModel

class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True

product1 = Product(id=101, name="Laptop", price=999.99)
print(product1)

product2 = Product(id=102, name="Smartphone", price=499.49, in_stock=False)
print(product2)

# product3 = Product(name="Tablet")
# print(product3)