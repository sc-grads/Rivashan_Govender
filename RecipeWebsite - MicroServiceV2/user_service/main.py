from fastapi import FastAPI, Depends, Form, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from routers.user import router as user_router
from models import Base
from fastapi.middleware.cors import CORSMiddleware
from schemas import UserInDBResponse
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
from fastapi.staticfiles import StaticFiles
import schemas
#from schemas import UserCreate,UserInDBResponse,UserUpdate
#from crud import get_user,get_user_by_email,create_user,update_user,delete_user

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Password hashing using bcrypt
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 token URL for authentication (you can create a token route separately)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app.include_router(user_router)

templates = Jinja2Templates(directory="main_app/Frontend/templates")



@app.post("/users/register/")
def register(
    username: str = Form(...), 
    email: str = Form(...), 
    password: str = Form(...), 
    db: Session = Depends(get_db)
):
    hashed_password =  pwd_context.hash(password)
    new_user = models.User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully"}




@app.post("/users/login")
def login(request: schemas.LoginRequest, db: Session = Depends(get_db)):
    # Fetch the user by username
    user = db.query(models.User).filter(models.User.username == request.username).first()

    # Validate user and password
    if not user or not pwd_context.verify(request.password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # If successful, return a success message
    return {"message": "Login successful", "user_id": user.id}




@app.get("/user/list")
def get_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    return users

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Simulated function to check if user is logged in
def get_current_user(token: str = Depends(oauth2_scheme)):
    if not token or token != "valid_token":  # Replace with your actual validation logic
        return None
    return {"username": "example_user"}  # Simulated user data

@app.get("/account")
async def account_page(request: Request, current_user: dict = Depends(get_current_user)):
    if not current_user:
        # If no user is logged in, redirect to the login page
        return RedirectResponse(url="/login")

    # If the user is logged in, render the account page
    return {"message": f"Welcome {current_user['username']} to your account!"}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)