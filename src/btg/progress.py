# src/btg/progress.py
from time import sleep, time

from src.btg.estimator import Estimator
from src.btg.fetcher import BTGTransactionFetcher
from src.config import Config


class ProgressTracker:
    def track_progress(
        self, txid, start_time=None, confirmation_target=Config.CONFIRMATION_TARGET
    ):
        fetcher = BTGTransactionFetcher(txid)
        estimator = Estimator()

        start_time = start_time or time()
        while True:
            data = fetcher.fetch_transaction_data()
            if data:
                current_confirmations = data.get("confirmations", 0)
                confirmation_rate = current_confirmations / (time() - start_time)
                time_left = estimator.estimate_time(
                    current_confirmations, confirmation_target, confirmation_rate
                )

                yield current_confirmations, time_left

            sleep(Config.POLLING_INTERVAL)

    def track_web_progress(
        self, txid, start_time=None, confirmation_target=Config.CONFIRMATION_TARGET
    ):
        fetcher = BTGTransactionFetcher(txid)
        estimator = Estimator()

        start_time = start_time or time()
        data = fetcher.fetch_transaction_data()
        if data:
            current_confirmations = data.get("confirmations", 0)
            confirmation_rate = current_confirmations / (time() - start_time)
            time_left = estimator.estimate_time(
                current_confirmations, confirmation_target, confirmation_rate
            )
            return {
                "current_confirmations": current_confirmations,
                "time_left": time_left,
                "confirmation_target": confirmation_target,
            }
