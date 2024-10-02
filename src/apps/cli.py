# src/apps/cli.py
import time

from tqdm import tqdm

from src.btg.progress import ProgressTracker
from src.config import Config


def cli_progress(txid, start_time=None, confirmation_target=None):
    if not confirmation_target:
        confirmation_target = Config.CONFIRMATION_TARGET

    print(f"Tracking transaction: {txid}")
    tracker = ProgressTracker()
    pbar = tqdm(total=confirmation_target, desc="Confirmations")

    for current_confirmations, time_left in tracker.track_progress(
        txid, start_time, confirmation_target
    ):
        pbar.n = current_confirmations
        pbar.refresh()
        print(f"Estimated time left: {time_left:.2f} minutes")

        if current_confirmations >= confirmation_target:
            print("\nTransaction confirmed!")
            break
        time.sleep(Config.POLLING_INTERVAL)
