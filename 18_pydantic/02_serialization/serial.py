from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street: str
    city: str
    zip_code: str

class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    created_at: datetime
    addresses: List[Address]
    tags: List[str]

    model_config = ConfigDict(json_encoders={datetime: lambda v: v.isoformat()})

user = User(
    id=1,
    name="John Doe",
    email="gS9cE@example.com",
    is_active=True,
    created_at=datetime.now(),
    addresses=[
        Address(street="123 Main St", city="Anytown", zip_code="12345"),
        Address(street="456 Maple Ave", city="Othertown", zip_code="67890")
    ],
    tags=["user", "admin", "developer"]
)

print(user.model_dump)
print(user.model_dump_json(indent=4))