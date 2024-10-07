from fastapi import APIRouter, FastAPI, Response, status, HTTPException, Form, Request, UploadFile, File
from sqlalchemy.orm import Session
from fastapi.params import Depends
from fastapi.security import OAuth2PasswordBearer
from starlette.responses import RedirectResponse
from ..database import get_db
from .. import models, schemas
from typing import List
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import List 
from passlib.context import CryptContext
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="Frontend/templates")

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

router = APIRouter()



#Button Functions
@router.get("/login", response_class=HTMLResponse)
def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@router.get("/register", response_class=HTMLResponse)
def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})


#Routing Functions
#@router.post('/login', response_model= schemas.DisplayUser)
#def login(request: schemas.User, db: Session = Depends(get_db)):
#    hashed_password = pwd_context.hash(request.password)
#    new_user = models.User(username = request.username, email = request.email, password = hashed_password)
#    db.add(new_user)
#    db.commit()
#    db.refresh(new_user)
#    return new_user

@router.post("/register")
def register(username: str = Form(...), email: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    hashed_password =  pwd_context.hash(password)
    new_user = models.User(username=username, email=email, password=hashed_password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return RedirectResponse(url="/login", status_code=303)

@router.post("/login")
def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    
    if user is None or not pwd_context.verify(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    return RedirectResponse(url="/products", status_code=303)