from pydantic import BaseModel
from typing import Optional, Union


class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class Company(BaseModel):
    name: str
    address: Optional[Address] = None


class Employee(BaseModel):
    id: int
    name: str
    company: Optional[Company] = None


addr = Address(street="123 Main St", city="Anytown", postal_code="12345")
comp = Company(name="Tech Corp", address=addr)
emp = Employee(id=1, name="John Doe", company=comp)
print(emp)


class TextContent(BaseModel):
    type_: str = "text"
    content: str


class ImageContent(BaseModel):
    type_: str = "image"
    url: str
    caption: Optional[str] = None


class Article(BaseModel):
    title: str
    sections: list[Union[TextContent, ImageContent]]


class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Address1(BaseModel):
    street: str
    city: City

class Organization(BaseModel):
    name: str
    headquarters: Address1
    branches: Optional[list[Address]] = None