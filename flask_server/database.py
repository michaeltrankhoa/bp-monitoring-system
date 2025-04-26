# app/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from app.models import Base
from config import Config

engine = create_engine(Config.DB_URI, echo=True)
SessionLocal = scoped_session(sessionmaker(bind=engine))

def init_db():
    Base.metadata.create_all(bind=engine)
