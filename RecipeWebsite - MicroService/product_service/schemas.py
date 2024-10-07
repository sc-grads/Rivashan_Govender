from pydantic import BaseModel
from .models import Product
class Product(BaseModel):
    name: str
    description: str
    price: int
    image: bytes 


class DisplayProduct(BaseModel):
    name:str
    description: str
    class Config:
        orm_mode = True

