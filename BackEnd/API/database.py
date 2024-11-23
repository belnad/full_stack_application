# database.py

from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base # type: ignore
from sqlalchemy.orm import sessionmaker # type: ignore
from dotenv import load_dotenv # type: ignore
import os


load_dotenv()

USER = os.environ.get("POSTGRES_USER")
HOST= os.environ.get("POSTGRES_HOST")
PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB = os.environ.get("POSTGRES_DB")


DATABASE_URL = f"mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB}"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Dependencies for the session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()