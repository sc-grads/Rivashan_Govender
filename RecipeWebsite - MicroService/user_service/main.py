from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import engine, get_db
from routers.user import router as user_router
from models import Base
from schemas import UserCreate,UserInDBResponse,UserUpdate
from crud import get_user,get_user_by_email,create_user,update_user,delete_user

Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(user_router, prefix="/users", tags=["users"])

@app.post("/register/", response_model=UserInDBResponse)
def create_user(user:UserCreate, db: Session = Depends(get_db)):
    db_user = get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return create_user(db=db, user=user)

@app.get("/users/{user_id}", response_model=UserInDBResponse)
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

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8002)