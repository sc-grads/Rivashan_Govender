from sqlalchemy import Column, Integer, DECIMAL, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class OrderDetails(Base):
    __tablename__ = 'orderdetails_tb'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    total = Column(DECIMAL, nullable=False)
    payment_id = Column(Integer, ForeignKey('paymentdetails_tb.id'))

    items = relationship("OrderItems", back_populates="order")

class OrderItems(Base):
    __tablename__ = 'orderitems_tb'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, ForeignKey('orderdetails_tb.id'), nullable=False)
    product_id = Column(Integer, nullable=False)

    order = relationship("OrderDetails", back_populates="items")