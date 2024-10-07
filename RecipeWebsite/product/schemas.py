from pydantic import BaseModel
from product.models import Product
class Product(BaseModel):
    name: str
    description: str
    price: int


class DisplayProduct(BaseModel):
    name:str
    description: str
    class Config:
        orm_mode = True

#Login Schemas
class User(BaseModel):
    username: str
    email: str
    password: str

class DisplayUser(BaseModel):
    username: str
    email: str
    class Config:
        orm_mode = True
