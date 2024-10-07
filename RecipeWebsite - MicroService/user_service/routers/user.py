from fastapi import APIRouter, Response, status, HTTPException, Form, Request, Depends
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import RedirectResponse
from database import get_db
import models
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates
from typing import List

templates = Jinja2Templates(directory="Frontend/templates")

# Password hashing using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 token URL for authentication (you can create a token route separately)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()

# Button Functions
@router.get("/login", response_class=HTMLResponse)
def login_form(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
def register_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


# User Registration
@router.post("/register")
def register(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Check if the user already exists
    user_exists = db.query(models.User).filter(models.User.username == username).first()
    if user_exists:
        raise HTTPException(status_code=400, detail="Username already registered")

    # Hash the password
    hashed_password = pwd_context.hash(password)
    
    # Create new user object
    new_user = models.User(username=username, email=email, password=hashed_password)
    
    # Add to the database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    # Redirect to login after successful registration
    return RedirectResponse(url="/login", status_code=303)


# User Login
@router.post("/login")
def login(
    username: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    # Query the database for the user
    user = db.query(models.User).filter(models.User.username == username).first()
    
    # Validate the user and password
    if user is None or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # If successful, redirect to the products page
    return RedirectResponse(url="/products", status_code=303)


# Authentication-related dependencies (for token-based authentication)
# Example token verification function:
def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password):
    return pwd_context.hash(password)

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    # You would decode and verify your token here, and return the user object
    user = db.query(models.User).filter(models.User.token == token).first()
    if user is None:
        raise HTTPException(status_code=401, detail="Invalid token")
    return user
