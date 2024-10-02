# src/btg/fetcher.py
import logging

import requests

from src.config import Config


class BTGTransactionFetcher:
    def __init__(self, txid: str):
        self.txid = txid
        self.api_url = f"{Config.API_URL}/tx/{txid}"

    def fetch_transaction_data(self):
        try:
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            logging.error(f"Error fetching transaction data: {e}")
            return None
