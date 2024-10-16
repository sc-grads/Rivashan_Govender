from typing import List
from fastapi import APIRouter, HTTPException, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from pydantic import BaseModel, EmailStr
from database import get_db
import models
import schemas

templates = Jinja2Templates(directory="main_app/Frontend/templates")


# Password hashing configuration
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Router instance for user-related routes
router = APIRouter()

# Pydantic schema for user registration
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

    class Config:
        from_attributes = True  # Pydantic V2 configuration

# Pydantic schema for user response (to hide sensitive data like password)
class UserResponse(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True  # Pydantic V2 configuration

# User Registration Route
@router.post("/users/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the user already exists
    user_in_db = db.query(models.User).filter(models.User.email == user.email).first()
    if user_in_db:
        raise HTTPException(status_code=400, detail="Email is already registered")

    # Hash the password
    hashed_password = pwd_context.hash(user.password)

    # Create a new user object
    new_user = models.User(username=user.username, email=user.email, password=hashed_password)

    # Add the user to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Return the user response (excluding password)
    return new_user

# User Login Route
class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/users/login")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    # Fetch the user by username
    user = db.query(models.User).filter(models.User.username == request.username).first()

    # Validate user and password
    if not user or not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # If successful, return a success message
    return {"message": "Login successful", "user_id": user.id}



# User list route for debugging purposes (optional)
@router.get("/user/list")
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users
