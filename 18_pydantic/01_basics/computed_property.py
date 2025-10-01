from pydantic import BaseModel, computed_field , Field

class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity

class Booking(BaseModel):
    user_id: int
    room_id: int
    nights: int = Field(..., ge=1)
    price_per_night: float = Field(..., gt=0)

    @computed_field
    @property
    def total_price(self) -> float:
        return self.nights * self.price_per_night

booking = Booking(user_id=1, room_id=101, nights=3, price_per_night=150.0)
print(booking.total_price)
print(booking.model_dump())  # total_price is included in the model dump
