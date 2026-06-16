"""Service-oriented scan orchestration helpers."""

import datetime

from app.core.engine import Engine
from app.core.database import Database


class ScanService:
    def __init__(self, db: Database | None = None):
        self.db = db or Database()

    def run_scan(self, ip: str, deep: bool = False) -> dict:
        result = {
            "ip": ip,
            "ts": datetime.datetime.now().isoformat(),
            "deep": deep,
            "private": Engine.is_private(ip),
            "class": Engine.ip_class(ip) if hasattr(Engine, "ip_class") else "UNKNOWN",
            "binary": Engine.binary(ip) if hasattr(Engine, "binary") else "",
            "hex": Engine.hexip(ip) if hasattr(Engine, "hexip") else "",
            "octal": Engine.octal(ip) if hasattr(Engine, "octal") else "",
            "integer": Engine.integer(ip) if hasattr(Engine, "integer") else 0,
            "md5": Engine.md5(ip),
            "sha1": Engine.sha1(ip),
            "sha256": Engine.sha256(ip),
            "rdns": Engine.rev_dns(ip) if hasattr(Engine, "rev_dns") else None,
            "hostname": Engine.get_hostname(),
            "fqdn": Engine.get_fqdn(),
            "local_ip": Engine.get_local_ip(),
            "cloud": Engine.cloud(ip),
            "open_ports": {},
            "threat": Engine.threat_score(ip),
            "shodan": Engine.shodan_query(ip),
        }
        for port in [21, 22, 23, 80, 443, 445, 8080, 8443]:
            if Engine.scan_port(ip, port, timeout=1.0 if not deep else 1.5):
                result["open_ports"][port] = {"svc": Engine.PORTS.get(port, ("Unknown", "Unknown"))[0], "desc": Engine.PORTS.get(port, ("Unknown", "Unknown"))[1], "banner": Engine.banner(ip, port)}
        self.db.save_scan(ip, result, result["threat"]["score"], result["threat"]["level"])
        self.db.track_session(ip)
        return result
