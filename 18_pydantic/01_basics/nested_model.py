from typing import Optional, List
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    addresses: Address


addr = Address(street="123 Main St", city="Anytown", postal_code="12345")
user = User(id=1, name="John Doe", email="gS9cE@example.com", addresses=addr)
print(user)

user_data = {
    "id": 2,
    "name": "Jane Smith",
    "addresses": {
        "street": "456 Elm St",
        "city": "Othertown",
        "postal_code": "67890"
    }
}
user2 = User(**user_data)
print(user2)