"""Simple JSON-based configuration management for the modular app."""

import json
from pathlib import Path

DEFAULT_CONFIG = {
    "app_name": "VIPER-EYE",
    "app_version": "3.1.0",
    "timeout": 2.0,
    "deep_scan": False,
    "log_level": "INFO",
}


class ConfigManager:
    def __init__(self, path: str = "config.json"):
        self.path = Path(path)
        self.data = dict(DEFAULT_CONFIG)
        self.load()

    def load(self) -> dict:
        if self.path.exists():
            try:
                self.data.update(json.loads(self.path.read_text(encoding="utf-8")))
            except Exception:
                pass
        return self.data

    def save(self) -> None:
        self.path.write_text(json.dumps(self.data, indent=2), encoding="utf-8")

    def get(self, key: str, default=None):
        return self.data.get(key, default)

    def set(self, key: str, value) -> None:
        self.data[key] = value
