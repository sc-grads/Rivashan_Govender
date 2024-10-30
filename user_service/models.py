from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base,relationship
from database import Base
from enum import Enum as PyEnum


Base = declarative_base()

# Enum for status and role constraints
class Status(PyEnum):
    ACTIVE = "active"
    INACTIVE = "inactive"

class Role(PyEnum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    EMPLOYEE = "employee"


class User(Base):
    __tablename__ = 'user_tb'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    telephone = Column(Integer)
    status = Column(Enum(Status), default=Status.INACTIVE, nullable=False)
    role = Column(Enum(Role), default=Role.CUSTOMER, nullable=False)
    
class ShoppingSession(Base):
    __tablename__ = 'session_tb'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=False)
    total = Column(Integer, nullable=False)