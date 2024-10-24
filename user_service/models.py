from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base
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
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(Enum(Status), default=Status.INACTIVE, nullable=False)
    role = Column(Enum(Role), default=Role.CUSTOMER, nullable=False)