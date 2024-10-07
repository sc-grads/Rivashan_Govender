from fastapi import FastAPI,Form
from pydantic import BaseModel, Field, HttpUrl
from typing import Set, List
from uuid import UUID
from datetime import date, datetime, timedelta

class Profile(BaseModel):
    name: str
    email: str
    age: int

class Product(BaseModel):
    name:str
    id: int
    price: int
    discount:int
    discounted_price: int

class User(BaseModel):
    name: str
    email: str


app = FastAPI()

@app.post('/login')
def login(username:str = Form(...), password:str=  Form(...)):
    return{'username': username}

@app.post('/purchase')
def purchase(user: User, product: Product):
    return{'user': user, 'product': product}

@app.post('/addproduct')
def addproduct(product: Product):
    product.discounted_price = product.price - (product.price * product.discount / 100)
    return product


@app.get('/')
def index():
    return {"Hello": "World"}

@app.get('/products')
def products(id: int | None = None, price: int | None = None) -> dict[str, str]:
    return {f"Product with an id: {id} and price {price}"}

@app.get('/profile/{userid}/{commentid}')
def profile(userid: int, commentid: int) -> dict[str, str]:
    return {f"Profile page for user with user id {userid} and comment with {commentid}"}

@app.post('/adduser')
def adduser(profile: Profile):
    return {'user_data'}
