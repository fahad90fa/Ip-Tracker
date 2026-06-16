"""Utility helpers for structured reports and summaries."""

import json


class ReportService:
    @staticmethod
    def summary(scan_result: dict) -> str:
        threat = scan_result.get("threat", {})
        return json.dumps({
            "ip": scan_result.get("ip"),
            "score": threat.get("score", 0),
            "level": threat.get("level", "UNKNOWN"),
            "open_ports": len(scan_result.get("open_ports", {})),
        }, indent=2)
