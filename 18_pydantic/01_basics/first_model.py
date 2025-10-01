from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    age: int = Field(..., ge=0, le=120)
    email: str
    is_active: bool = True

# Example usage
try:
    user = User(id=1, name="Alice", age=30, email="BqM0G@example.com")
    print(user)
except ValueError as e:
    print("Validation error:", e)