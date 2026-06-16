"""Modular launcher for the existing GUI application."""

import argparse

from app.core.config_manager import ConfigManager
from app.core.logger import AppLogger
from app.services.scan_service import ScanService


def main() -> None:
    parser = argparse.ArgumentParser(description="VIPER-EYE modular launcher")
    parser.add_argument("--target", default="8.8.8.8", help="IP or hostname to inspect")
    parser.add_argument("--deep", action="store_true", help="Run an extended scan")
    args = parser.parse_args()

    config = ConfigManager("config.json")
    logger = AppLogger("viper_eye", "viper_eye.log").get_logger()
    logger.info("Starting modular scan for %s deep=%s", args.target, args.deep)

    result = ScanService().run_scan(args.target, deep=args.deep)
    print("SCAN RESULT:")
    print(result)
    print("SUMMARY:")
    print(f"Threat score: {result.get('threat', {}).get('score', 0)} | Level: {result.get('threat', {}).get('level', 'UNKNOWN')}")


if __name__ == "__main__":
    main()
