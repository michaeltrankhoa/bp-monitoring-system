# app/routes/heart_rate_routes.py
from flask import Blueprint, request, jsonify # type: ignore
from app.services.heart_rate_service import record_heart_rate, get_latest_heart_rate

heart_rate_bp = Blueprint("heart_rate_bp", __name__, url_prefix="/api/heart_rate")


@heart_rate_bp.route("/", methods=["POST"])
def add_heart_rate():
    data = request.get_json()
    try:
        heart_rate = data.get("heart_rate")
        result = record_heart_rate(heart_rate)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@heart_rate_bp.route("/", methods=["GET"])
def list_heart_rate():
    try:
        data = get_latest_heart_rate()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
