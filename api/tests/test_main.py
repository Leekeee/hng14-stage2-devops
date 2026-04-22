from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import app

client = TestClient(app)

@patch("main.r")
def test_submit_job(mock_redis):
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)
    response = client.post("/jobs")
    assert response.status_code == 201
    assert "job_id" in response.json()

@patch("main.r")
def test_get_job_not_found(mock_redis):
    mock_redis.hget = MagicMock(return_value=None)
    response = client.get("/jobs/fake-id")
    assert response.status_code == 200
    assert "error" in response.json()

@patch("main.r")
def test_get_job_found(mock_redis):
    mock_redis.hget = MagicMock(return_value=b"queued")
    response = client.get("/jobs/some-job-id")
    assert response.status_code == 200
    assert response.json()["status"] == "queued"
    
