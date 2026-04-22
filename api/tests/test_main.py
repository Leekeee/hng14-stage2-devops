from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

@patch("main.redis_client")
def test_submit_job(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)
    response = client.post("/jobs")
    assert response.status_code == 200
    assert "job_id" in response.json()

@patch("main.redis_client")
def test_get_jobs(mock_redis):
    mock_redis.hgetall = MagicMock(return_value={})
    mock_redis.keys = MagicMock(return_value=[])
    response = client.get("/jobs")
    assert response.status_code == 200

@patch("main.redis_client")
def test_health_check(mock_redis):
    mock_redis.ping = MagicMock(return_value=True)
    response = client.get("/health")
    assert response.status_code == 200
