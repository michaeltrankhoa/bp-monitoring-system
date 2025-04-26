# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret-key")
    # Ví dụ sử dụng SQLite; điều chỉnh DB_URI nếu dùng CSDL khác
    DB_URI = os.getenv("DB_URI", "sqlite:///vitals.db")
