import unittest
from unittest.mock import patch

from src.apps.cli import cli_progress


class TestCLIProgress(unittest.TestCase):

    @patch("src.btg.fetcher.BTGTransactionFetcher.fetch_transaction_data")
    def test_cli_progress(self, mock_fetch):
        mock_fetch.side_effect = [{"confirmations": 1}, {"confirmations": 300}]
        cli_progress("test_txid", start_time="0", confirmation_target=300)

        # Assert that the function finishes without errors
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
