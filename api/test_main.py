import pytest
from unittest.mock import patch, MagicMock
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# ─────────────────────────────────────────
# Mock Redis so tests don't need real Redis
# ─────────────────────────────────────────
@pytest.fixture
def mock_redis():
    with patch('main.r') as mock:
        yield mock


# ─────────────────────────────────────────
# TEST 1 - Health endpoint
# ─────────────────────────────────────────
def test_health_returns_200():
    """Health endpoint must return 200"""
    response = client.get("/health")
    assert response.status_code == 200


# ─────────────────────────────────────────
# TEST 2 - Health endpoint returns correct body
# ─────────────────────────────────────────
def test_health_returns_status_ok():
    """Health endpoint must return status ok"""
    response = client.get("/health")
    data = response.json()
    assert data["status"] == "ok"


# ─────────────────────────────────────────
# TEST 3 - Create job returns job_id
# ─────────────────────────────────────────
def test_create_job_returns_job_id(mock_redis):
    """Creating a job must return a job_id"""
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)
    response = client.post("/jobs")
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data


# ─────────────────────────────────────────
# TEST 4 - Create job returns 200
# ─────────────────────────────────────────
def test_create_job_returns_200(mock_redis):
    """Creating a job must return HTTP 200"""
    mock_redis.lpush = MagicMock(return_value=1)
    mock_redis.hset = MagicMock(return_value=1)
    response = client.post("/jobs")
    assert response.status_code == 200


# ─────────────────────────────────────────
# TEST 5 - Get job not found returns 404
# ─────────────────────────────────────────
def test_get_job_not_found_returns_404(mock_redis):
    """Getting non-existent job must return 404"""
    mock_redis.hget = MagicMock(return_value=None)
    response = client.get("/jobs/nonexistent-id")
    assert response.status_code == 404


# ─────────────────────────────────────────
# TEST 6 - Get existing job returns status
# ─────────────────────────────────────────
def test_get_existing_job_returns_status(mock_redis):
    """Getting existing job must return job_id and status"""
    mock_redis.hget = MagicMock(return_value=b"queued")
    response = client.get("/jobs/some-job-id")
    assert response.status_code == 200
    data = response.json()
    assert "job_id" in data
    assert "status" in data
    assert data["status"] == "queued"
