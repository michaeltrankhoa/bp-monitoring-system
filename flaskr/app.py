# flask_server/app.py
from flask import Flask, render_template, jsonify
import firebase_admin
from firebase_admin import credentials, firestore

app = Flask(__name__)

# Khởi tạo Firebase Admin SDK từ file chứng chỉ
cred = credentials.Certificate("bp-monitoring-system-d4552-firebase-adminsdk-fbsvc-f002cfc116.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


@app.route("/")
def index():
    # Render index.html
    return render_template("templates/index.html")


@app.route("/api/blood_pressure")
def get_blood_pressure_data():
    # Get data from collection "blood_pressure" in Firestore
    docs = db.collection("blood_pressure").stream()
    data = [doc.to_dict() for doc in docs]
    return jsonify(data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
