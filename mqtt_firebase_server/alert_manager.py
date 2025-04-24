# mqtt_firebase_server/alert_manager.py
from firebase_admin import firestore
import datetime

# Ví dụ: Ngưỡng báo động
THRESHOLDS = {
    "systolic": 140,
    "diastolic": 90,
    "heart_rate": 100
}

def check_and_create_alert(data, db):
    alerts = []
    if data["systolic"] > THRESHOLDS["systolic"]:
        alerts.append("Systolic vượt ngưỡng")
    if data["diastolic"] > THRESHOLDS["diastolic"]:
        alerts.append("Diastolic vượt ngưỡng")
    if data["heart_rate"] > THRESHOLDS["heart_rate"]:
        alerts.append("Nhịp tim vượt ngưỡng")
    
    if alerts:
        alert_message = "; ".join(alerts)
        alert_data = {
            "alert": alert_message,
            "data": data,
            "timestamp": datetime.datetime.now().isoformat()
        }
        # Lưu vào collection "alerts" trong Firestore
        db.collection("alerts").add(alert_data)
        return alert_data
    return None
