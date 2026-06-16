"""Core scanning and intelligence helpers."""

import hashlib
import json
import platform
import random
import re
import socket
import struct
import subprocess
import time
import urllib.error
import urllib.request
from collections import OrderedDict

from app.config import DEFAULT_TIMEOUT


class Engine:
    """Lightweight scanning and intelligence utilities used by the GUI."""

    PORTS = {
        21: ("FTP", "File Transfer Protocol"),
        22: ("SSH", "Secure Shell"),
        23: ("Telnet", "Telnet Protocol"),
        25: ("SMTP", "Simple Mail Transfer"),
        53: ("DNS", "Domain Name System"),
        80: ("HTTP", "Hypertext Transfer Protocol"),
        110: ("POP3", "Post Office Protocol v3"),
        135: ("MSRPC", "Microsoft RPC"),
        139: ("NetBIOS", "NetBIOS Session Service"),
        143: ("IMAP", "Internet Message Access"),
        161: ("SNMP", "Simple Network Management"),
        443: ("HTTPS", "HTTP over TLS/SSL"),
        445: ("SMB", "Server Message Block"),
        502: ("Modbus", "SCADA Protocol"),
        6379: ("Redis", "Redis Key-Value Store"),
        8080: ("HTTP-Alt", "HTTP Alternate/Proxy"),
        8443: ("HTTPS-Alt", "HTTPS Alternate"),
    }

    PRIVATE = [("10.0.0.0", "10.255.255.255"), ("172.16.0.0", "172.31.255.255"), ("192.168.0.0", "192.168.255.255")]

    @staticmethod
    def ip2int(ip: str) -> int:
        try:
            return struct.unpack("!I", socket.inet_aton(ip))[0]
        except Exception:
            return 0

    @staticmethod
    def int2ip(value: int) -> str:
        try:
            return socket.inet_ntoa(struct.pack("!I", value))
        except Exception:
            return "0.0.0.0"

    @staticmethod
    def valid_ip(ip: str) -> bool:
        try:
            socket.inet_aton(ip)
            return len(ip.split(".")) == 4 and all(0 <= int(part) <= 255 for part in ip.split("."))
        except Exception:
            return False

    @staticmethod
    def ip_class(ip: str) -> str:
        first = int(ip.split(".")[0]) if Engine.valid_ip(ip) else 0
        if 1 <= first <= 126:
            return "A"
        if 128 <= first <= 191:
            return "B"
        if 192 <= first <= 223:
            return "C"
        if 224 <= first <= 239:
            return "D (Multicast)"
        return "E (Reserved)"

    @staticmethod
    def binary(ip: str) -> str:
        return ".".join(format(int(part), "08b") for part in ip.split("."))

    @staticmethod
    def hexip(ip: str) -> str:
        return format(Engine.ip2int(ip), "08X")

    @staticmethod
    def octal(ip: str) -> str:
        return ".".join(format(int(part), "04o") for part in ip.split("."))

    @staticmethod
    def integer(ip: str) -> int:
        return Engine.ip2int(ip)

    @staticmethod
    def rev_dns(ip: str) -> str | None:
        try:
            hostname, _, _ = socket.gethostbyaddr(ip)
            return hostname
        except Exception:
            return None

    @staticmethod
    def resolve(host: str) -> str | None:
        try:
            return socket.gethostbyname(host)
        except Exception:
            return None

    @staticmethod
    def scan_port(ip: str, port: int, timeout: float = DEFAULT_TIMEOUT) -> bool:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            sock.close()
            return result == 0
        except Exception:
            return False

    @staticmethod
    def banner(ip: str, port: int, timeout: float = DEFAULT_TIMEOUT) -> str | None:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((ip, port))
            sock.send(b"\r\n")
            data = sock.recv(1024).decode("utf-8", errors="ignore").strip()
            sock.close()
            return data[:300] or None
        except Exception:
            return None

    @staticmethod
    def md5(value: str) -> str:
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    @staticmethod
    def sha1(value: str) -> str:
        return hashlib.sha1(value.encode("utf-8")).hexdigest()

    @staticmethod
    def sha256(value: str) -> str:
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    @staticmethod
    def get_local_ip() -> str:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.connect(("8.8.8.8", 80))
            ip = sock.getsockname()[0]
            sock.close()
            return ip
        except Exception:
            return "127.0.0.1"

    @staticmethod
    def get_hostname() -> str:
        return socket.gethostname()

    @staticmethod
    def get_fqdn() -> str:
        return socket.getfqdn()

    @staticmethod
    def threat_score(ip: str, geo_data: dict | None = None, bl: list | None = None, tor: bool = False) -> dict:
        score = 0
        reasons = []
        if bl:
            score += min(len(bl) * 12, 40)
            reasons.append("Listed on blacklist")
        if tor:
            score += 30
            reasons.append("Tor exit node detected")
        if geo_data and geo_data.get("proxy"):
            score += 20
            reasons.append("Proxy/VPN detected")
        if geo_data and geo_data.get("hosting"):
            score += 10
            reasons.append("Hosting/datacenter")
        if Engine.is_private(ip):
            return {"score": 0, "level": "LOW", "reasons": ["Private/internal IP"]}
        score = max(0, min(100, score))
        level = "LOW" if score <= 20 else "MODERATE" if score <= 50 else "HIGH" if score <= 75 else "CRITICAL"
        return {"score": score, "level": level, "reasons": reasons or ["No threat indicators"]}

    @staticmethod
    def is_private(ip: str) -> bool:
        value = Engine.ip2int(ip)
        for start, end in Engine.PRIVATE:
            if Engine.ip2int(start) <= value <= Engine.ip2int(end):
                return True
        return False

    @staticmethod
    def cloud(ip: str) -> str | None:
        return None

    @staticmethod
    def blacklist(ip: str) -> list:
        return []

    @staticmethod
    def tor_check(ip: str) -> bool:
        return False

    @staticmethod
    def shodan_query(ip: str) -> dict | None:
        try:
            url = "https://internetdb.shodan.io/" + ip
            req = urllib.request.Request(url, headers={"User-Agent": "VIPER-EYE/3.1"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except Exception:
            return None

    @staticmethod
    def extract_ips_from_text(text: str) -> list[str]:
        pattern = r"\b(?:\d{1,3}\.){3}\d{1,3}\b"
        return [ip for ip in re.findall(pattern, text) if Engine.valid_ip(ip)]

    @staticmethod
    def generate_tracker_link(domain: str = "example.com", path: str = "/track") -> dict:
        uid = hashlib.md5(str(time.time()).encode("utf-8")).hexdigest()[:10]
        return {"link": f"https://{domain}{path}?id={uid}", "id": uid, "created": time.time()}
