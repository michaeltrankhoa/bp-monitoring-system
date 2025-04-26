# simulator/simulator.py
import paho.mqtt.client as mqtt
import json
import time
import random
from datetime import datetime

# MQTT broker configuration
broker = "mqtt.fuvitech.vn"  # MQTT broker address
port = 1883
topic = "blood_pressure/data"

client = mqtt.Client("BP_Simulator")
client.connect(broker, port)

while True:
  # Generate random blood pressure data
	systolic = random.randint(90, 140)  # SBP
	diastolic = random.randint(60, 90)  # DBP
	heart_rate = random.randint(60, 100)  # HR
	spo2 = random.randint(95, 100)  # SpO2
	measurement_time = datetime.now().isoformat()
	payload = {
		"systolic": systolic,
		"diastolic": diastolic,
		"heart_rate": heart_rate,
		"spo2": spo2,
		"timestamp": measurement_time,
	}
	# Push data to MQTT topic
	client.publish(topic, json.dumps(payload))
	print(f"Sent: {payload}")
	time.sleep(5)
