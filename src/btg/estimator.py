# src/btg/estimator.py
import logging

from src.config import Config


class Estimator:
    def estimate_time(
        self, current_confirmations, confirmation_target, confirmation_rate
    ):
        if current_confirmations >= confirmation_target:
            logging.info("Transaction already confirmed!")
            return 0
        remaining_confirmations = confirmation_target - current_confirmations
        time_left = remaining_confirmations / confirmation_rate
        logging.info(f"Estimated time left: {time_left:.2f} minutes")
        return time_left
