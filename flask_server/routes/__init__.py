# app/routes/__init__.py
from app.routes.bp_routes import bp_bp
from app.routes.heart_rate_routes import heart_rate_bp
from app.routes.spo2_routes import spo2_bp
from app.routes.co_routes import co_bp

def register_routes(app):
    app.register_blueprint(bp_bp)
    app.register_blueprint(heart_rate_bp)
    app.register_blueprint(spo2_bp)
    app.register_blueprint(co_bp)
