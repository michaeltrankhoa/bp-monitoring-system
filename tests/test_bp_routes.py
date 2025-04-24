# tests/test_bp_routes.py
import json
import pytest
from app import create_app
from app.database import init_db


@pytest.fixture
def client():
  app = create_app()
  app.config["TESTING"] = True
  init_db()  # Khởi tạo lại cơ sở dữ liệu cho test
  with app.test_client() as client:
  	yield client


def test_add_bp(client):
  data = {"dbp": 80, "sbp": 120}
  response = client.post("/api/bp/", json=data)
  assert response.status_code == 201
  json_data = response.get_json()
  assert "message" in json_data
