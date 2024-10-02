from unittest.mock import MagicMock, patch

import pytest

from src.btg.progress import ProgressTracker


@pytest.fixture
def mock_fetcher():
    with patch("src.btg.progress.BTGTransactionFetcher") as mock:
        yield mock


@pytest.fixture
def mock_estimator():
    with patch("src.btg.progress.Estimator") as mock:
        yield mock


def test_track_progress(mock_fetcher, mock_estimator):
    tracker = ProgressTracker()
    mock_fetcher_instance = mock_fetcher.return_value
    mock_fetcher_instance.fetch_transaction_data.side_effect = [
        {"confirmations": 1},
        {"confirmations": 2},
        {"confirmations": 3},
        {"confirmations": 300},
    ]
    mock_estimator_instance = mock_estimator.return_value
    mock_estimator_instance.estimate_time.return_value = 10

    results = list(tracker.track_progress("test_txid"))

    assert len(results) == 4
    assert results[0][0] == 1
    assert results[1][0] == 2
    assert results[2][0] == 3
    assert results[3][0] == 300


def test_track_web_progress(mock_fetcher, mock_estimator):
    tracker = ProgressTracker()
    mock_fetcher_instance = mock_fetcher.return_value
    mock_fetcher_instance.fetch_transaction_data.return_value = {"confirmations": 150}

    result = tracker.track_web_progress("test_txid")

    assert result["current_confirmations"] == 150
