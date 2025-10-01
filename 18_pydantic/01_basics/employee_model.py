from pydantic import BaseModel, Field
from typing import Optional

class Employee(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=100)
    age: int = Field(..., ge=18, le=65)
    email: str
    position: Optional[str] = None
    is_full_time: bool = True