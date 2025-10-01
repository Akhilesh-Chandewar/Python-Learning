from pydantic import BaseModel
from typing import List, Dict, Optional

class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
    discount_code: Optional[str] = None
    total_price: float

class BlogPost(BaseModel):
    title: str
    content: str
    img_url: Optional[str] = None

cart_data = {
    "user_id": 1,
    "items": ["apple", "banana", "orange"],
    "quantities": {"apple": 2, "banana": 3, "orange": 1},
    "total_price": 15.75    
}

cart = Cart(**cart_data)
print(cart)