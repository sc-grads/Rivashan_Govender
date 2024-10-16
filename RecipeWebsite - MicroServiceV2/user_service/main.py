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

"""@app.post("/users/register/", response_model=UserInDBResponse)
def register(user:UserInDBResponse, db: Session = Depends(get_db)):
    return register(db=db, user=user)
"""
    


"""@app.get("/users/{user_id}", response_model=UserInDBResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}", response_model=UserInDBResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return update_user(db=db, db_user=db_user, user=user)

@app.delete("/users/{user_id}", response_model=UserInDBResponse)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return delete_user(db=db, db_user=db_user)
"""
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)