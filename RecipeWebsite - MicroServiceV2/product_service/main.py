import asyncio
import os
from fastapi import FastAPI, APIRouter, File, Form, HTTPException, Depends, Request, UploadFile,status
from typing import List, Optional
from models import Base, Product
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from schemas import ProductCreate, ProductRead, ProductResponse  # Pydantic schemas for validation
from database import SessionLocal, get_db, engine  # Import your DB session dependency
import base64
from routers.product import router as product_router# Create the database tables

Base.metadata.create_all(bind=engine)

# Initialize the FastAPI app
app = FastAPI()

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this in production for security purposes
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Set up Jinja2 templates
templates = Jinja2Templates(directory="main_app/Frontend/templates")


app.include_router(product_router)


# Route to display the catalog of products
#@app.get("/product/list")
#def get_products(request: Request, db: Session = Depends(get_db)):
#    products = db.query(Product).all()
#    for product in products:
#        if product.image:
#            product.image = base64.b64encode(product.image).decode('utf-8')
#    return products



# Route to add a new product
@app.post( "/product/add", response_model=ProductCreate, status_code=status.HTTP_201_CREATED)
def add(name: str = Form(...), 
    description: str = Form(...), 
    price: float = Form(...), 
    image: UploadFile = File(...), 
    db: Session = Depends(get_db)
):
    image_data = image.file.read()  # Read the uploaded image
    db = SessionLocal()
    new_product = Product(name=name, description=description, price=price, image=image_data)
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product


# Route to delete a product by its ID
@app.delete("/delete/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    db.delete(product)
    db.commit()
    return {"message": "Product deleted successfully"}


@app.put("/update/{product_id}", response_model=ProductResponse)
def update_product(
    product_id: int,
    product_data: ProductCreate,
    db: Session = Depends(get_db),
):
    product = db.query(Product).filter(Product.id == product_id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    product.name = product_data.name
    product.price = product_data.price
    product.description = product_data.description
    product.image = product_data.image  # Update image URL from frontend

    db.commit()
    db.refresh(product)
    return product

# Run the app using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
