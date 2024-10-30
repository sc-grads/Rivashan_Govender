from datetime import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey, Enum, LargeBinary
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum

class ActionEnum(PyEnum):
    PURCHASE = "purchase"
    RETURN = "return"
    RETURN_WITH_REFUND = "return with refund"
    RETURN_WITH_REPLACEMENT = "return with replacement"


class Product(Base):
    __tablename__ = "product_tb"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    desc = Column(String)
    SKU = Column(String, unique=True)
    category = Column(String)
    price = Column(Float, nullable=False)
    image = Column(LargeBinary)



    order_histories = relationship("OrderHistory", back_populates="product")



class OrderHistory(Base):
    __tablename__ = "order_hist_tb"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product_tb.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_tb.id'), nullable=False)  # Link to the User table
    total = Column(Float, nullable=False)
    action = Column(Enum(ActionEnum), nullable=False)  # Enum for action
    timestamp = Column(DateTime, default=datetime.utcnow)  # Time of the action

    # Relationships
    product = relationship("Product", back_populates="order_histories")
    user = relationship("User")  # Assuming you have a User model