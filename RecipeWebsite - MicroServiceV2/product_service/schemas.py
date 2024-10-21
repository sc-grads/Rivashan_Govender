from fastapi import File, UploadFile
from pydantic import BaseModel
from typing import Optional

class ProductBase(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    image: bytes

class ProductCreate(ProductBase):
    name: str
    description: Optional[str] = None
    price: float  
    image: Optional[UploadFile] = File(None)
class ProductRead(ProductBase):
    id: int

    class Config:
        orm_mode = True

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: str

    class Config:
        orm_mode = True  # To convert SQLAlchemy models to Pydantic objects