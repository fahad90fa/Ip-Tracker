"""Rotating logger setup for the modular app."""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path


class AppLogger:
    def __init__(self, name: str = "viper_eye", log_file: str = "viper_eye.log"):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.INFO)
        if not self.logger.handlers:
            handler = RotatingFileHandler(Path(log_file), maxBytes=5 * 1024 * 1024, backupCount=5)
            handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)s %(name)s %(message)s"))
            self.logger.addHandler(handler)

    def get_logger(self):
        return self.logger
