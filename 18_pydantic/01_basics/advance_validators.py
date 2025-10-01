from pydantic import BaseModel, field_validator , model_validator
from datetime import datetime

class Person(BaseModel):
    first_name: str
    last_name: str

    @field_validator('first_name', 'last_name', mode='before')
    def capitalize_names(cls, value):
        if not value.istitle():
            raise ValueError('Name must start with a capital letter')
        return value.capitalize()

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"

class user(BaseModel):
    email: str

    @field_validator('email')
    def normalize_email(cls, value):
        return value.lower().strip()

class Product(BaseModel):
    price: str

    @field_validator('price', mode='before')
    def validate_price(cls, value):
        if isinstance(value, str) and value.startswith('$'):
            return float(value[1:])
        raise ValueError('Price must be a string starting with $')
        return float(value)

class DateRange(BaseModel):
    start_date: datetime
    end_date: datetime

    @model_validator(mode='after')
    def validate_date_range(cls , values):
        if values.end_date <= values.start_date:
            raise ValueError('end_date must be after start_date')
        return values
