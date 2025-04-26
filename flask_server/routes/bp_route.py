# flask_server/routes/bp_route.py
from flask import Blueprint, request, jsonify
from flask_server.services.bp_service import record_bp, get_latest_bp

bp_bp = Blueprint('bp_bp', __name__, url_prefix='/api/bp')

@bp_bp.route('/', methods=['POST'])
def add_bp():
    data = request.get_json()
    try:
        # Dữ liệu đầu vào mong đợi: {"dbp": 80, "sbp": 120}
        dbp = data.get("dbp")
        sbp = data.get("sbp")
        result = record_bp(dbp, sbp)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@bp_bp.route('/', methods=['GET'])
def list_bp():
    try:
        data = get_latest_bp()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 400
