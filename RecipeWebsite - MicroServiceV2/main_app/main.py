from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os
from typing import List

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust as needed for your security requirements
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

static_dir = os.path.join(os.path.dirname(__file__), 'static')

app.mount("/static", StaticFiles(directory=static_dir), name="static")

templates = Jinja2Templates(directory="Frontend/templates")



@app.get("/")
async def read_root(request: Request):
    return templates.TemplateResponse("HomePage.html", {"request": request})

@app.get("/users")
async def read_users():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8002")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="User service error")
    return response.json()

@app.get("/product")
async def read_products():
    async with httpx.AsyncClient() as client:
        response = await client.get("http://localhost:8001")
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code, detail="Product service error")
    return response.json()



@app.get("/user/list", response_class=HTMLResponse)
def users_page(request: Request):
    return templates.TemplateResponse("users.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/catalog", response_class=HTMLResponse)
def products_page(request: Request):
    return templates.TemplateResponse("products.html", {"request": request})


@app.get("/register")
async def register_page(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.get("/add-product")
async def add_product_page(request: Request):
    return templates.TemplateResponse("add-product.html", {"request": request})

@app.get("/cart")
async def cart_page(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})

@app.get("/account")
async def cart_page(request: Request):
    return templates.TemplateResponse("account.html", {"request": request})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)