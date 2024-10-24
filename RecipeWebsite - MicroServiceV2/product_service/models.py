import datetime
from sqlalchemy import Column, DateTime, Integer, String, Float, ForeignKey, Enum, LargeBinary
from sqlalchemy.orm import relationship
from database import Base
from enum import Enum as PyEnum


class Product(Base):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    image = Column(LargeBinary)


class ActionEnum(PyEnum):
    PURCHASE = "purchase"
    RETURN = "return"
    RETURN_WITH_REFUND = "return with refund"
    RETURN_WITH_REPLACEMENT = "return with replacement"


class OrderHistory(Base):
    __tablename__ = "order_hist"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)  # Link to the User table
    total = Column(Float, nullable=False)
    action = Column(Enum(ActionEnum), nullable=False)  # Enum for action
    timestamp = Column(DateTime, default=datetime.utcnow)  # Time of the action

    # Relationships
    product = relationship("Product", back_populates="order_histories")
    user = relationship("User")  # Assuming you have a User model