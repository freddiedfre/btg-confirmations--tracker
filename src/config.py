# src/config.py
import os


class Config:
    API_URL = os.getenv("BTG_API_URL", "http://localhost:3001/api")
    POLLING_INTERVAL = int(os.getenv("POLLING_INTERVAL", 60))
    CONFIRMATION_TARGET = int(os.getenv("CONFIRMATION_TARGET", 300))
