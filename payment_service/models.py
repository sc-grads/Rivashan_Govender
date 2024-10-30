from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()



class PaymentDetails(Base):
    __tablename__ = 'paymentdetail_tb'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(Integer, nullable=False)
    amount = Column(Integer, nullable=False)
    provider = Column(String)
    status = Column(String, default= "pending")