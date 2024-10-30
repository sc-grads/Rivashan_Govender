

from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class CartItem(Base):
    __tablename__ = 'cart_item'

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey('session_tb.id'))
    product_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)