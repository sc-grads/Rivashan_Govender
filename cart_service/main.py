from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from sqlalchemy.orm import Session
from database import get_db, engine, Base
from models import CartItem
import schemas

# Initialize FastAPI app
app = FastAPI()

# Create the database tables if they don't exist
Base.metadata.create_all(bind=engine)

# In-memory cart to simulate a simple data store (Replace with DB in production)
cart_db = []

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cart/", response_model=schemas.CartItem)
def add_to_cart(item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    """Add an item to the cart."""
    new_item = CartItem(product_id=item.product_id, quantity=item.quantity)
    db.add(new_item)
    db.commit()
    db.refresh(new_item)
    return new_item


@app.get("/cart/", response_model=List[schemas.CartItem])
def get_cart(db: Session = Depends(get_db)):
    """Get all items in the cart."""
    items = db.query(CartItem).all()
    return items


@app.delete("/cart/{item_id}", response_model=dict)
def delete_cart_item(item_id: int, db: Session = Depends(get_db)):
    """Remove an item from the cart."""
    item = db.query(CartItem).filter(CartItem.id == item_id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return {"message": f"Item {item_id} deleted successfully"}


@app.delete("/cart/clear", response_model=dict)
def clear_cart(db: Session = Depends(get_db)):
    """Clear the entire cart."""
    db.query(CartItem).delete()
    db.commit()
    return {"message": "Cart cleared successfully"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8003)