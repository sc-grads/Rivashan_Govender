from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Payment as PaymentModel  # Assuming you have a Payment model defined
import schemas
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI app
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Create a new payment
@app.post("/payments/", response_model=schemas.Payment)
def create_payment(payment: schemas.PaymentCreate, db: Session = Depends(get_db)):
    db_payment = PaymentModel(
        user_id=payment.user_id,
        order_id=payment.order_id,
        amount=payment.amount,
        payment_method=payment.payment_method,
        status="pending"  # Set initial status to pending
    )
    db.add(db_payment)
    db.commit()
    db.refresh(db_payment)
    return db_payment

# Retrieve a payment by ID
@app.get("/payments/{payment_id}", response_model=schemas.Payment)
def read_payment(payment_id: int, db: Session = Depends(get_db)):
    payment = db.query(PaymentModel).filter(PaymentModel.id == payment_id).first()
    if payment is None:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment

# Retrieve all payments for a user
@app.get("/users/{user_id}/payments/", response_model=schemas.PaymentList)
def read_user_payments(user_id: int, db: Session = Depends(get_db)):
    payments = db.query(PaymentModel).filter(PaymentModel.user_id == user_id).all()
    return schemas.PaymentList(payments=payments)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8005)
