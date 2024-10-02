from unittest.mock import MagicMock, patch

import pytest

from src.btg.fetcher import BTGTransactionFetcher


@pytest.fixture
def fetcher():
    return BTGTransactionFetcher("test_txid")


@patch("src.btg.fetcher.requests.get")
def test_fetch_transaction_data_success(mock_get, fetcher):
    mock_response = MagicMock()
    mock_response.json.return_value = {"confirmations": 5}
    mock_response.raise_for_status = MagicMock()
    mock_get.return_value = mock_response

    result = fetcher.fetch_transaction_data()

    assert result == {"confirmations": 5}
    mock_get.assert_called_once_with(
        "http://localhost:3001/api/tx/test_txid", timeout=10
    )


@patch("src.btg.fetcher.requests.get")
def test_fetch_transaction_data_failure(mock_get, fetcher):
    mock_get.side_effect = Exception("Network error")

    result = fetcher.fetch_transaction_data()

    assert result is None
