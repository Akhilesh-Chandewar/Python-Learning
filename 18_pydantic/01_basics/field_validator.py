from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    name: str
    age: int

    @field_validator('age')
    def check_age(cls, value):
        if value < 0:
            raise ValueError('Age must be a non-negative integer')
        if value > 120:
            raise ValueError('Age must be less than or equal to 120')
        return value
    
    @field_validator('name')
    def check_name(cls, value):
        if not value.isalpha():
            raise ValueError('Name must contain only alphabetic characters')
        return value.title()
    
# Example usage
try:
    user = User(name="johndoe", age=25)
    print(user)
except ValueError as e:
    print(f"Validation error: {e}")

class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode='after')
    def passwords_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError('Passwords do not match')
        return values