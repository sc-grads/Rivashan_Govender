from pydantic import BaseModel, Field
from typing import List, Optional

# Schema for a product to be added to the cart
class CartItemBase(BaseModel):
    product_id: int = Field(..., description="ID of the product")
    quantity: int = Field(..., gt=0, description="Quantity of the product")

# Schema for creating a cart item (request)
class CartItemCreate(CartItemBase):
    pass  # No extra fields for creating the cart item

# Schema for updating the quantity of a cart item
class CartItemUpdate(BaseModel):
    quantity: int = Field(..., gt=0, description="Updated quantity of the product")

# Schema for the response when retrieving a cart item
class CartItem(CartItemBase):
    id: int = Field(..., description="ID of the cart item")
    cart_id: int = Field(..., description="ID of the associated cart")

    class Config:
        orm_mode = True  # Enables ORM to Pydantic model conversion

# Schema for the entire cart (e.g., when fetching all items in a cart)
class Cart(BaseModel):
    id: int = Field(..., description="ID of the cart")
    user_id: int = Field(..., description="ID of the user who owns the cart")
    items: List[CartItem] = Field(default_factory=list, description="List of items in the cart")

    class Config:
        orm_mode = True
