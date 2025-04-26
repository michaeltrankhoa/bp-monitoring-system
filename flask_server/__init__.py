# app/__init__.py
from flask import Flask
from app.config.config import Config
from app.database import init_db
from app.routes import register_routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Khởi tạo cơ sở dữ liệu (tạo bảng nếu chưa có)
    init_db()

    # Đăng ký các blueprint từ thư mục routes
    register_routes(app)
    
    return app
