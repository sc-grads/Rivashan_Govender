import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Setting up the base directory and database path
#BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#DATABASE_PATH = os.path.join(BASE_DIR, '../data/Recipe.db')

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./data/Recipe.db"

# Creating the SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# Creating the sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for declarative models
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
