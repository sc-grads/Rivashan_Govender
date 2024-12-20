import base64
from typing import List, Optional

from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from models import Product
from schemas import ProductCreate, ProductRead, ProductResponse
from sqlalchemy.orm import Session
from database import SessionLocal, get_db 
from fastapi import APIRouter, File, Form, HTTPException, Depends, Request, UploadFile,status
from pydantic import BaseModel

router = APIRouter()

class ProductRead(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image: Optional[bytes]

    class Config:
        from_attributes = True 

templates = Jinja2Templates(directory="main_app/Frontend/templates")



@router.get("/product/list")
def get_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(Product).all()
    for product in products:
        if product.image:
            product.image = base64.b64encode(product.image).decode('utf-8')
    return products


@router.post("/product/add", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def add_product(
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    try:
        image_data = await image.read()
        new_product = Product(
            name= name,
            description= description,
            price= price,
            image= image_data,
        )
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return {"message": "Product added successfully", "product": new_product}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error adding product: {str(e)}")


@router.get("product/{product_id}", response_model=ProductRead)
def read_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.delete("product/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}

