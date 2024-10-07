from fastapi import APIRouter, Response, status, HTTPException, Form, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from product_service import models, schemas
from typing import List
from fastapi.templating import Jinja2Templates
import base64

templates = Jinja2Templates(directory="main_app\Frontend\templates")

router = APIRouter()

# Button Functions
@router.get("/add-product")
def add_product_form(request: Request):
    return templates.TemplateResponse("add-product.html", {"request": request})

@router.get("/update", response_class=HTMLResponse)
def update_form(request: Request):
    return templates.TemplateResponse("update.html", {"request": request})

@router.get("/cart", response_class=HTMLResponse)
def addtocart_form(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})


#########################################

@router.put('/product/{id}')
def update_product(id: int, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product Not Found")
    
    product.update(request.dict())
    db.commit()
    return {"Success": "Recipe Updated"}

# Deleting Product
@router.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product not found")

    db.delete(product)
    db.commit()
    return {"status": "success"}

# Get All Products
@router.get("/products", response_class=HTMLResponse)
def get_products(request: Request, db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    for product in products:
        if product.image:
            product.image = base64.b64encode(product.image).decode('utf-8')
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

# Get Single Product
@router.get('/product/{id}', response_model=schemas.DisplayProduct)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID: {id} not found")
    return product

# Add Product with form submission and image upload
@router.post("/add-product")
def add_product(
    request: Request,
    name: str = Form(...),
    description: str = Form(...),
    price: float = Form(...),
    image: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    image_data = image.file.read()
    new_product = models.Product(name=name, description=description, price=price, image=image_data)

    # Add the new product to the database
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # Redirect to the products page after successful submission
    return RedirectResponse(url="/products", status_code=303)

