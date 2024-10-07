import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Get the database URL from the environment variable, with a fallback
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./data/Recipe.db")

# Create a new SQLite engine
# Note: We remove pool_size and max_overflow as they're not applicable to SQLite
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False},  # Needed for SQLite
    echo=False,  # Set to True if you want to see the raw SQL queries in logs
)

# Session creation
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    except SQLAlchemyError as e:
        print(f"Database Error: {e}")
        db.rollback()  # Rollback if there was an error
    finally:
        db.close()  # Ensure the session is closed after the request