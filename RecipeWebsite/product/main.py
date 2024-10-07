from fastapi import FastAPI, Request
from .import models
from .database import engine
from typing import List 
from .database import get_db
from .routers import product, user
from fastapi.templating import Jinja2Templates

app = FastAPI()

models.Base.metadata.create_all(engine)

templates = Jinja2Templates(directory="Frontend/templates")


app.include_router(product.router)
app.include_router(user.router)
#Customers Routes

