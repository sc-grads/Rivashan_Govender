from pydantic import BaseModel, Field
from typing import List, Optional

# Schema for a payment request
class PaymentBase(BaseModel):
    user_id: int = Field(..., description="ID of the user making the payment")
    order_id: int = Field(..., description="ID of the order being paid for")
    amount: float = Field(..., gt=0, description="Amount to be paid")
    payment_method: str = Field(..., description="Payment method used (e.g., credit card, PayPal)")

# Schema for creating a payment (request)
class PaymentCreate(PaymentBase):
    pass  # No extra fields for creating the payment

# Schema for the response when retrieving a payment
class Payment(PaymentBase):
    id: int = Field(..., description="ID of the payment transaction")
    status: str = Field(..., description="Status of the payment (e.g., completed, pending, failed)")

    class Config:
        orm_mode = True  # Enables ORM to Pydantic model conversion

# Schema for a list of payments (e.g., when fetching all payments for a user)
class PaymentList(BaseModel):
    payments: List[Payment] = Field(default_factory=list, description="List of payment transactions")
