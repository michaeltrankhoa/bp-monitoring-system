# mqtt_firebase_server/mqtt_listener.py
import paho.mqtt.client as mqtt
import json
import firebase_admin
from firebase_admin import credentials, firestore

# Khởi tạo Firebase Admin với file chứng chỉ
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

broker = "mqtt.fuvitech.vn"  # Địa chỉ MQTT broker
port = 1883
topic = "blood_pressure/data"


# Hàm callback khi kết nối thành công với broker
def on_connect(client, userdata, flags, rc):
	print("Kết nối MQTT thành công, code:", rc)
	client.subscribe(topic)


# Hàm callback khi nhận được message từ broker
def on_message(client, userdata, msg):
	try:
		data = json.loads(msg.payload.decode())
		# Lưu dữ liệu vào Firestore trong collection "blood_pressure"
		db.collection("blood_pressure").add(data)
		print("Data was written into Firebase:", data)

		# (Tùy chọn) Thêm logic kiểm tra ngưỡng bất thường
		# if data["systolic"] > 140 or data["diastolic"] > 90:
		#     # Gửi cảnh báo (Email, SMS, hoặc thông báo đẩy)
		#     pass
	except Exception as e:
		print("Data error:", e)


client = mqtt.Client("Firebase_Server")
client.on_connect = on_connect
client.on_message = on_message

client.connect(broker, port, 60)
client.loop_forever()
