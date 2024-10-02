from unittest.mock import MagicMock, patch

import pytest

from src.apps.web import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


@pytest.fixture
def mock_progress_tracker():
    with patch("src.btg.progress.ProgressTracker") as mock:
        yield mock


def test_web_form_get(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"form" in response.data


def test_web_form_post(mock_progress_tracker, client):
    mock_tracker_instance = mock_progress_tracker.return_value
    mock_tracker_instance.track_web_progress.return_value = {
        "current_confirmations": 100,
        "time_left": 5,
        "confirmation_target": 300,
    }

    response = client.post("/", data={"txid": "test_txid"})
    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["current_confirmations"] == 100
