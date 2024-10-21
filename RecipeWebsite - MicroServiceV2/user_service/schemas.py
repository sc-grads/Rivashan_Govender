from pydantic import BaseModel, EmailStr, Field
from typing import Optional
from datetime import datetime

class User(BaseModel):
    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    password: str = Field(..., min_length=8)

# User Login Routedocker
class LoginRequest(BaseModel):
    email: str
    password: str


    class Config:
        orm_mode = True  # Change this from orm_mode to from_attributes

# Alias for response model
UserInDBResponse = User

