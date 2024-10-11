"""from sqlalchemy.orm import Session
from passlib.context import CryptContext
from models import User
from schemas import UserCreate, UserUpdate
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, user:UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user =User(email=user.email, username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, db_user:User, user:UserUpdate):
    update_data = user.dict(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_user, key, value)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, db_user:User):
    db.delete(db_user)
    db.commit()
    return db_user"""