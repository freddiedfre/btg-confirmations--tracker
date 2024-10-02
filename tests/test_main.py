import pytest

from src.main import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_form_page(client):
    """Test that the form page renders correctly."""
    response = client.get("/")
    assert response.status_code == 200


def test_submit_form(client, mocker):
    """Test submitting the form."""
    mocker.patch("src.btg.progress.ProgressTracker.track_progress", return_value=None)
    response = client.post("/", data={"txid": "mock_txid", "confirmation_target": 300})
    assert response.status_code == 200
