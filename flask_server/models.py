# app/models.py
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class VitalSigns(Base):
	__tablename__ = "vital_signs"
	id = Column(Integer, primary_key=True)
	dbp = Column(Integer, nullable=True)         # Huyết áp tâm trương
	sbp = Column(Integer, nullable=True)         # Huyết áp tâm thu
	heart_rate = Column(Integer, nullable=True)    # Nhịp tim
	spo2 = Column(Integer, nullable=True)          # SpO₂ - độ bão hòa oxy
	co = Column(Float, nullable=True)              # Cardiac Output
	timestamp = Column(DateTime, default=datetime.utcnow)
