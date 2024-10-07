from fastapi import APIRouter,FastAPI, Response, status, HTTPException, Form, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db
from .. import models, schemas, database
from typing import List
from fastapi.templating import Jinja2Templates
import base64

templates = Jinja2Templates(directory="Frontend/templates")


router = APIRouter()


#Button Functions
@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@router.get("/add-product")
def add_product_form(request: Request):
    return templates.TemplateResponse("add-product.html", {"request": request})


@router.put('/product/{id}')
def update(id, request: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id)
    if not product.first():
        return {'Error': 'Product Not Found'}
    product.update(request.dict())
    db.commit()
    return {'Success': 'Recipe Updated'}


#@router.delete('/product/{id}')
#def delete( id, db: Session = Depends(get_db)):
#    product = db.query(models.Product).filter(models.Product.id == id).delete(synchronize_session=False)
#   db.commit()
#    return {'Deleted meal from Menu'}





#Deleting Product
@router.delete("/products/{product_id}")
async def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"status": "success"}

@router.get("/products")
def products(request: Request, db: Session = Depends(get_db)):
    products = db.query(models.Product).all()
    for product in products:
        if product.image:
            product.image = base64.b64encode(product.image).decode('utf-8')
    return templates.TemplateResponse("products.html", {"request": request, "products": products})

#@router.get("/products")
#def products(request: Request, db: Session = Depends(get_db)):  
    # Fetch all products from the database
    #products = db.query(models.Product).all()
    #return templates.TemplateResponse("products.html", {"request": request, "products": products})

@router.get( '/product/{id}', response_model= schemas.DisplayProduct)
def product( id, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Product with ID: {id} not found")
    return product

@router.post( '/product')
def add(  name: str, description: str, price: float, image: UploadFile = File(...), db: Session = Depends(get_db)):
    image_data = image.file.read()
    new_product = models.Product(
        name = name, description = description, price = price, image = image_data)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product




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
    new_product = models.Product(name=name, description=description, price=price, image = image_data)

    # Add the new product to the database
    db.add(new_product)
    db.commit()
    db.refresh(new_product)

    # Redirect to the products page after successful submission
    return RedirectResponse(url="/products", status_code=303)

