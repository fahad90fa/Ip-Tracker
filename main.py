#!/usr/bin/env python3
"""
███████╗██████╗ ██╗ ██████╗ ███████╗███████╗███████╗
██╔════╝██╔══██╗██║██╔════╝ ██╔════╝██╔════╝██╔════╝
█████╗  ██████╔╝██║██║  ███╗█████╗  ███████╗███████╗
██╔══╝  ██╔══██╗██║██║   ██║██╔══╝  ╚════██║╚════██║
██║     ██║  ██║██║╚██████╔╝███████╗███████║███████║
╚═╝     ╚═╝  ╚═╝╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝
                    ⚡ VIPER-EYE ⚡
       ULTIMATE IP Intelligence & Tracking Suite
                    v3.0.0
"""

import tkinter as tk
from tkinter import ttk, messagebox, font as tkfont, filedialog
import socket
import struct
import subprocess
import threading
import json
import os
import sys
import time
import datetime
import re
import hashlib
import platform
import urllib.request
import urllib.error
import math
import random
import ipaddress
import csv
import io
import base64
import sqlite3
import zipfile
import tempfile
import shutil
from collections import OrderedDict

# ════════════════════════════════════════════════════════════════
# PALETTE
# ════════════════════════════════════════════════════════════════

class C:
    VOID = "#05050a"
    ABYSS = "#08080f"
    DEEP = "#0b0b16"
    PANEL = "#0f0f1e"
    CARD = "#111128"
    INPUT = "#15152d"
    BORDER = "#1a1a3a"
    GLOW_G = "#00ff88"
    GLOW_C = "#00e5ff"
    GLOW_R = "#ff0044"
    GLOW_O = "#ff6600"
    GLOW_Y = "#ffcc00"
    GLOW_P = "#b040ff"
    GLOW_PK = "#ff0088"
    GLOW_W = "#ffffff"
    TXT = "#d0d0e8"
    TXT2 = "#6a6a9a"
    TXT3 = "#3a3a6a"
    DIM = "#222244"

# ════════════════════════════════════════════════════════════════
# MAC VENDOR DATABASE (TOP 200)
# ════════════════════════════════════════════════════════════════

MAC_VENDORS = {
    "001122": "Cisco Systems", "0011B8": "Cisco Systems", "001319": "Cisco Systems",
    "001A2B": "Cisco Systems", "001B54": "Cisco Systems", "001C58": "Cisco Systems",
    "001E4A": "Cisco Systems", "001EF5": "Cisco Systems", "00219A": "Cisco Systems",
    "00226B": "Cisco Systems", "0023EB": "Cisco Systems", "0024C7": "Cisco Systems",
    "002545": "Cisco Systems", "0025B5": "Cisco Systems", "00260B": "Cisco Systems",
    "000C29": "VMware Inc", "001C14": "VMware Inc", "005056": "VMware Inc",
    "000D3A": "VMware Inc", "0016E0": "VMware Inc",
    "F8BC12": "Apple Inc", "3C22FB": "Apple Inc", "A4B197": "Apple Inc",
    "AC87A3": "Apple Inc", "78CA39": "Apple Inc", "B8E856": "Apple Inc",
    "D4619D": "Samsung Electronics", "507AC5": "Samsung Electronics",
    "B47443": "Samsung Electronics", "A0CBFD": "Samsung Electronics",
    "8C16D1": "Samsung Electronics", "DC2B2A": "Samsung Electronics",
    "001C42": "Fortinet Inc", "704DC1": "Fortinet Inc",
    "001E0B": "Fortinet Inc", "005013": "Fortinet Inc",
    "001BD4": "Fortinet Inc", "005312": "Fortinet Inc",
    "0018F2": "Fortinet Inc", "005515": "Fortinet Inc",
    "001A6C": "Fortinet Inc", "005617": "Fortinet Inc",
    "001AA9": "Fortinet Inc", "005730": "Fortinet Inc",
    "001CC0": "Fortinet Inc", "005822": "Fortinet Inc",
    "001E65": "Fortinet Inc", "005930": "Fortinet Inc",
    "001E90": "Fortinet Inc", "005A13": "Fortinet Inc",
    "0004ED": "Fortinet Inc", "005B18": "Fortinet Inc",
    "000C29": "Fortinet Inc", "005C1D": "Fortinet Inc",
    "0021F7": "Fortinet Inc", "005D22": "Fortinet Inc",
    "0023E9": "Fortinet Inc", "005E27": "Fortinet Inc",
    "00259C": "Fortinet Inc", "005F2C": "Fortinet Inc",
    "00260B": "Fortinet Inc", "006031": "Fortinet Inc",
    "0027D4": "Fortinet Inc", "006136": "Fortinet Inc",
    "0028E9": "Fortinet Inc", "00623B": "Fortinet Inc",
    "0029E9": "Fortinet Inc", "006340": "Fortinet Inc",
    "002A0E": "Fortinet Inc", "006445": "Fortinet Inc",
    "002B1E": "Fortinet Inc", "00654A": "Fortinet Inc",
    "002C2E": "Fortinet Inc", "00664F": "Fortinet Inc",
    "002D3E": "Fortinet Inc", "006754": "Fortinet Inc",
    "002E4E": "Fortinet Inc", "006859": "Fortinet Inc",
    "002F5E": "Fortinet Inc", "00695E": "Fortinet Inc",
    "00306E": "Fortinet Inc", "006A63": "Fortinet Inc",
    "00317E": "Fortinet Inc", "006B68": "Fortinet Inc",
    "00328E": "Fortinet Inc", "006C6D": "Fortinet Inc",
    "00339E": "Fortinet Inc", "006D72": "Fortinet Inc",
    "0034AE": "Fortinet Inc", "006E77": "Fortinet Inc",
    "0035BE": "Fortinet Inc", "006F7C": "Fortinet Inc",
    "0036CE": "Fortinet Inc", "007081": "Fortinet Inc",
    "0037DE": "Fortinet Inc", "007186": "Fortinet Inc",
    "0038EE": "Fortinet Inc", "00728B": "Fortinet Inc",
    "0039FE": "Fortinet Inc", "007390": "Fortinet Inc",
    "003A0E": "Fortinet Inc", "007495": "Fortinet Inc",
    "003B1E": "Fortinet Inc", "00759A": "Fortinet Inc",
    "003C2E": "Fortinet Inc", "00769F": "Fortinet Inc",
    "003D3E": "Fortinet Inc", "0077A4": "Fortinet Inc",
    "003E4E": "Fortinet Inc", "0078A9": "Fortinet Inc",
    "003F5E": "Fortinet Inc", "0079AE": "Fortinet Inc",
    "B499BA": "Intel Corporation", "F46D04": "Intel Corporation",
    "3C970E": "Intel Corporation", "70B5E8": "Intel Corporation",
    "B0ECEB": "Intel Corporation", "A46706": "Intel Corporation",
    "2CBE08": "Intel Corporation", "1CCDE3": "Intel Corporation",
    "B0A7B9": "Intel Corporation", "F8B156": "Intel Corporation",
    "E4B39D": "Intel Corporation", "F0DEB1": "Intel Corporation",
    "000FFB": "Intel Corporation", "0013CE": "Intel Corporation",
    "0017C4": "Intel Corporation", "0019D1": "Intel Corporation",
    "001E64": "Intel Corporation", "001EB9": "Intel Corporation",
    "00215C": "Intel Corporation", "0024D6": "Intel Corporation",
    "0026B9": "Intel Corporation", "002710": "Intel Corporation",
    "3C5282": "Hewlett Packard", "2C41A1": "Hewlett Packard",
    "1CC1DE": "Hewlett Packard", "3CA10F": "Hewlett Packard",
    "2CDDA5": "Hewlett Packard", "0C2345": "Hewlett Packard",
    "10604B": "Hewlett Packard", "D48564": "Hewlett Packard",
    "001B78": "Dell Inc", "F8DB88": "Dell Inc", "B88303": "Dell Inc",
    "001E4F": "Dell Inc", "002219": "Dell Inc", "00248C": "Dell Inc",
    "002561": "Dell Inc", "001C23": "Dell Inc", "0024E8": "Dell Inc",
    "E83935": "Huawei Technologies", "C8BA94": "Huawei Technologies",
    "5C7D5E": "Huawei Technologies", "A8D6E3": "Huawei Technologies",
    "782BDC": "Huawei Technologies", "B0F1EC": "Huawei Technologies",
    "EC9BF0": "Huawei Technologies", "8CA97E": "Huawei Technologies",
    "DC8B28": "Netgear", "9C3DCF": "Netgear", "C43DC7": "Netgear",
    "6038E0": "Netgear", "008EF2": "Netgear", "A42B8C": "Netgear",
    "24B2DE": "Netgear", "C0FFD4": "Netgear", "9459AD": "Netgear",
    "803773": "Netgear", "A02195": "Netgear", "00336D": "Netgear",
    "0026F2": "Netgear", "E0469A": "Netgear", "6CB8C1": "Netgear",
    "C89E43": "Netgear", "003F7D": "Netgear", "A42BB0": "Netgear",
    "B03956": "Netgear", "E894F6": "Netgear", "04A151": "Netgear",
    "04BD70": "Netgear", "504A6E": "Netgear", "C4A81D": "Netgear",
    "6038E0": "Netgear", "E4F46C": "Netgear", "C0D6AA": "Netgear",
    "B077AC": "Netgear", "58EF68": "Netgear", "8C8401": "Netgear",
    "E89EF7": "Netgear", "6CB8C1": "Netgear", "E0469A": "Netgear",
    "D8B837": "TP-LINK", "1062EB": "TP-LINK", "7CC2C6": "TP-LINK",
    "5C628B": "TP-LINK", "A842A1": "TP-LINK", "B0A7B9": "TP-LINK",
    "5CE931": "TP-LINK", "F8D111": "TP-LINK", "ACDCE5": "TP-LINK",
    "C006C3": "TP-LINK", "7DA7B1": "TP-LINK", "9C5322": "TP-LINK",
    "B0BEC5": "TP-LINK", "E848B8": "TP-LINK", "50C7BF": "TP-LINK",
    "1097BD": "TP-LINK", "54AF97": "TP-LINK", "4C60DE": "TP-LINK",
    "704F57": "TP-LINK", "40329B": "TP-LINK", "5C628B": "TP-LINK",
    "7DA7B1": "TP-LINK", "9CA2F4": "TP-LINK", "A842A1": "TP-LINK",
    "B09928": "TP-LINK", "EC172F": "TP-LINK", "F0F9A0": "TP-LINK",
    "60E327": "TP-LINK", "B0BEC5": "TP-LINK", "7CC2C6": "TP-LINK",
    "A0F3C1": "TP-LINK", "50DCE7": "TP-LINK", "6CE873": "TP-LINK",
    "7DB2EF": "TP-LINK", "9CA2F4": "TP-LINK", "A842A1": "TP-LINK",
    "B09928": "TP-LINK", "EC172F": "TP-LINK", "F0F9A0": "TP-LINK",
    "000C29": "Fortinet Inc", "005056": "VMware Inc",
    "F8BC12": "Apple Inc", "D4619D": "Samsung Electronics",
    "B499BA": "Intel Corporation", "3C5282": "Hewlett Packard",
    "001B78": "Dell Inc", "E83935": "Huawei Technologies",
    "DC8B28": "Netgear", "D8B837": "TP-LINK",
}

# ════════════════════════════════════════════════════════════════
# IOT DEVICE SIGNATURES
# ════════════════════════════════════════════════════════════════

IOT_SIGNATURES = {
    554: ("RTSP", "IP Camera / CCTV", "HIGH"),
    8554: ("RTSP-Alt", "IP Camera / CCTV", "HIGH"),
    37777: ("Dahua", "Dahua CCTV", "HIGH"),
    34567: ("DVR", "DVR/NVR System", "HIGH"),
    8080: ("HTTP-Mgmt", "Camera/IoT Web UI", "MEDIUM"),
    8443: ("HTTPS-Mgmt", "Camera/IoT Web UI", "MEDIUM"),
    161: ("SNMP", "Network Device/IoT", "MEDIUM"),
    502: ("Modbus", "SCADA/ICS", "CRITICAL"),
    1883: ("MQTT", "IoT Broker", "HIGH"),
    5683: ("CoAP", "IoT/Constrained", "MEDIUM"),
    8883: ("MQTT-S", "IoT Broker SSL", "HIGH"),
    5353: ("mDNS", "IoT Discovery", "LOW"),
    1900: ("UPnP-SSDP", "IoT Discovery", "LOW"),
    62078: ("iDevice", "Apple Device Sync", "LOW"),
    5228: ("Android", "Android Debug", "MEDIUM"),
    27017: ("MongoDB", "IoT Database", "CRITICAL"),
    6379: ("Redis", "IoT Cache", "HIGH"),
    2375: ("Docker", "Docker API", "CRITICAL"),
    9000: ("PHP-FPM", "Web Server", "MEDIUM"),
    47808: ("BACnet", "Building Automation", "CRITICAL"),
}

# ════════════════════════════════════════════════════════════════
# OS FINGERPRINT DATABASE (TTL-based)
# ════════════════════════════════════════════════════════════════

OS_FINGERPRINTS = {
    (128, 64): ("Windows", "10/11", "NT 10.0"),
    (128, 32): ("Windows", "7/8", "NT 6.x"),
    (128, 128): ("Windows", "Server", "NT 6.x+"),
    (64, 64): ("Linux", "Kernel 2.4+", "2.4+"),
    (64, 32): ("Linux", "Older", "2.2"),
    (255, 64): ("FreeBSD", "11+", "11+"),
    (255, 255): ("FreeBSD", "Older", "10-"),
    (64, 60): ("macOS", "10+", "Darwin"),
    (64, 255): ("Solaris", "11", "SunOS"),
    (255, 64): ("OpenBSD", "6+", "6+"),
    (128, 255): ("AIX", "7", "7+"),
    (255, 32): ("HP-UX", "11", "11i"),
    (30, 30): ("iOS", "14+", "Darwin ARM"),
    (64, 30): ("Android", "10+", "Linux ARM"),
}

# ════════════════════════════════════════════════════════════════
# ENGINE v3
# ════════════════════════════════════════════════════════════════

class Engine:

    PORTS = {
        21: ("FTP", "File Transfer Protocol"), 22: ("SSH", "Secure Shell"),
        23: ("Telnet", "Telnet Protocol"), 25: ("SMTP", "Simple Mail Transfer"),
        53: ("DNS", "Domain Name System"), 80: ("HTTP", "Hypertext Transfer Protocol"),
        110: ("POP3", "Post Office Protocol v3"), 111: ("RPCBind", "RPC Bind Service"),
        135: ("MSRPC", "Microsoft RPC"), 139: ("NetBIOS", "NetBIOS Session Service"),
        143: ("IMAP", "Internet Message Access"), 161: ("SNMP", "Simple Network Management"),
        179: ("BGP", "Border Gateway Protocol"), 389: ("LDAP", "Lightweight Directory Access"),
        443: ("HTTPS", "HTTP over TLS/SSL"), 445: ("SMB", "Server Message Block"),
        502: ("Modbus", "SCADA Protocol"), 636: ("LDAPS", "LDAP over SSL"),
        873: ("Rsync", "Remote Sync"), 993: ("IMAPS", "IMAP over SSL"),
        995: ("POP3S", "POP3 over SSL"), 1080: ("SOCKS", "SOCKS Proxy"),
        1433: ("MSSQL", "Microsoft SQL Server"), 1521: ("Oracle", "Oracle DB Listener"),
        1723: ("PPTP", "Point-to-Point Tunneling"), 1883: ("MQTT", "IoT Broker"),
        2049: ("NFS", "Network File System"), 2222: ("SSH-Alt", "SSH Alternate"),
        2375: ("Docker", "Docker API"), 3306: ("MySQL", "MySQL Database"),
        3389: ("RDP", "Remote Desktop Protocol"), 4443: ("HTTPS-Alt", "HTTPS Alternate"),
        5000: ("UPnP", "Universal Plug and Play"), 5432: ("PostgreSQL", "PostgreSQL Database"),
        554: ("RTSP", "Real Time Streaming"), 5683: ("CoAP", "Constrained App Protocol"),
        5900: ("VNC", "Virtual Network Computing"), 6379: ("Redis", "Redis Key-Value Store"),
        6443: ("HTTPS-Alt2", "HTTPS Alternate 2"), 7777: ("HTTP-Alt", "HTTP Alternate"),
        8000: ("HTTP-Proxy", "HTTP Proxy"), 8080: ("HTTP-Alt", "HTTP Alternate/Proxy"),
        8443: ("HTTPS-Alt", "HTTPS Alternate"), 8554: ("RTSP-Alt", "RTSP Alternate"),
        8888: ("HTTP-Proxy", "HTTP Proxy"), 9000: ("PHP-FPM", "PHP FastCGI"),
        9090: ("Prometheus", "Prometheus Monitoring"), 9200: ("Elasticsearch", "Elasticsearch REST API"),
        9443: ("HTTPS-Alt3", "HTTPS Alternate 3"), 27017: ("MongoDB", "MongoDB Database"),
        34567: ("DVR", "DVR System"), 37777: ("Dahua", "Dahua CCTV"),
        11211: ("Memcached", "Memcached Cache"), 47808: ("BACnet", "Building Automation"),
    }

    BLACKLISTS = [
        "zen.spamhaus.org", "bl.spamcop.net", "dnsbl.sorbs.net",
        "b.barracudacentral.org", "dnsbl-1.uceprotect.net",
        "pbl.spamhaus.org", "sbl.spamhaus.org", "xbl.spamhaus.org",
        "cbl.abuseat.org", "dbl.spamhaus.org",
    ]

    TOR_DNSBL = "exitnodes.tor.dnsbl.sectoor.ch"

    CLOUD = {
        "AWS": [("3.0.0.0","3.127.255.255"),("3.128.0.0","3.255.255.255"),("4.0.0.0","4.31.255.255"),("13.224.0.0","13.254.255.255"),("15.0.0.0","15.255.255.255"),("18.0.0.0","18.255.255.255"),("34.0.0.0","34.255.255.255"),("35.0.0.0","35.255.255.255"),("52.0.0.0","52.95.255.255"),("54.0.0.0","54.255.255.255")],
        "Google Cloud": [("8.8.8.0","8.8.15.255"),("35.192.0.0","35.199.255.255"),("104.154.0.0","104.154.255.255"),("130.211.0.0","130.211.255.255")],
        "Azure": [("4.128.0.0","4.255.255.255"),("13.64.0.0","13.107.255.255"),("20.0.0.0","20.255.255.255"),("40.64.0.0","40.127.255.255")],
        "DigitalOcean": [("45.55.0.0","45.55.255.255"),("68.183.0.0","68.183.255.255"),("128.199.0.0","128.199.255.255"),("142.93.0.0","142.93.255.255"),("159.65.0.0","159.65.255.255")],
        "Linode": [("45.33.0.0","45.33.127.255"),("172.104.0.0","172.104.255.255"),("139.144.0.0","139.162.255.255")],
        "Vultr": [("45.32.0.0","45.77.255.255"),("66.42.0.0","66.42.255.255"),("104.156.224.0","104.238.255.255"),("149.28.0.0","149.28.255.255")],
        "Hetzner": [("5.9.0.0","5.9.255.255"),("78.46.0.0","78.47.255.255"),("88.198.0.0","88.198.255.255"),("136.243.0.0","136.243.255.255"),("159.69.0.0","159.69.255.255")],
        "OVH": [("5.39.0.0","5.39.255.255"),("46.105.0.0","46.105.255.255"),("51.68.0.0","51.68.255.255"),("91.134.0.0","91.134.255.255"),("164.132.0.0","164.132.255.255"),("176.31.0.0","176.31.255.255")],
    }

    PRIVATE = [("10.0.0.0","10.255.255.255"),("172.16.0.0","172.31.255.255"),("192.168.0.0","192.168.255.255"),("127.0.0.0","127.255.255.255"),("169.254.0.0","169.254.255.255")]

    @staticmethod
    def ip2int(ip):
        try: return struct.unpack("!I", socket.inet_aton(ip))[0]
        except: return 0

    @staticmethod
    def int2ip(n):
        try: return socket.inet_ntoa(struct.pack("!I", n))
        except: return "0.0.0.0"

    @staticmethod
    def valid_ip(ip):
        try:
            socket.inet_aton(ip)
            p = ip.split(".")
            return len(p) == 4 and all(0 <= int(x) <= 255 for x in p)
        except: return False

    @staticmethod
    def is_private(ip):
        n = Engine.ip2int(ip)
        for s, e in Engine.PRIVATE:
            if Engine.ip2int(s) <= n <= Engine.ip2int(e): return True
        return False

    @staticmethod
    def ip_class(ip):
        f = int(ip.split(".")[0])
        if 1 <= f <= 126: return "A"
        if 128 <= f <= 191: return "B"
        if 192 <= f <= 223: return "C"
        if 224 <= f <= 239: return "D (Multicast)"
        return "E (Reserved)"

    @staticmethod
    def binary(ip): return ".".join(format(int(o), "08b") for o in ip.split("."))

    @staticmethod
    def hexip(ip): return format(Engine.ip2int(ip), "08X")

    @staticmethod
    def octal(ip): return ".".join(format(int(o), "04o") for o in ip.split("."))

    @staticmethod
    def integer(ip): return Engine.ip2int(ip)

    @staticmethod
    def rev_dns(ip):
        try:
            h, _, _ = socket.gethostbyaddr(ip)
            return h
        except: return None

    @staticmethod
    def resolve(host):
        try: return socket.gethostbyname(host)
        except: return None

    @staticmethod
    def subnet(ip, cidr=24):
        ipn = Engine.ip2int(ip)
        mask = (0xFFFFFFFF << (32 - cidr)) & 0xFFFFFFFF
        net = ipn & mask
        bcast = net | (~mask & 0xFFFFFFFF)
        nh = (2 ** (32 - cidr)) - 2 if cidr >= 2 else 0
        return {"network": Engine.int2ip(net), "broadcast": Engine.int2ip(bcast),
                "mask": Engine.int2ip(mask), "wildcard": Engine.int2ip(~mask & 0xFFFFFFFF),
                "first": Engine.int2ip(net + 1) if nh > 0 else "N/A",
                "last": Engine.int2ip(bcast - 1) if nh > 0 else "N/A",
                "hosts": nh, "cidr": "/" + str(cidr)}

    @staticmethod
    def cloud(ip):
        n = Engine.ip2int(ip)
        for prov, ranges in Engine.CLOUD.items():
            for s, e in ranges:
                if Engine.ip2int(s) <= n <= Engine.ip2int(e): return prov
        return None

    @staticmethod
    def scan_port(ip, port, timeout=1.5):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            r = s.connect_ex((ip, port))
            s.close()
            return r == 0
        except: return False

    @staticmethod
    def banner(ip, port, timeout=2):
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(timeout)
            s.connect((ip, port))
            if port in (80, 8080, 8443, 8000, 8888):
                s.send(b"HEAD / HTTP/1.1\r\nHost: " + ip.encode() + b"\r\n\r\n")
            else:
                s.send(b"\r\n")
            b = s.recv(1024).decode("utf-8", errors="ignore").strip()
            s.close()
            return b[:300] if b else None
        except: return None

    @staticmethod
    def geo(ip):
        urls = [
            "http://ip-api.com/json/" + ip + "?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,asname,mobile,proxy,hosting",
            "https://ipinfo.io/" + ip + "/json",
        ]
        for url in urls:
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "VIPER-EYE/3.0"})
                with urllib.request.urlopen(req, timeout=8) as resp:
                    d = json.loads(resp.read().decode("utf-8"))
                    if d.get("status") == "success" or d.get("country"):
                        lat = d.get("lat", 0)
                        lon = d.get("lon", 0)
                        if not lat and "loc" in d:
                            pts = str(d["loc"]).split(",")
                            lat = pts[0] if len(pts) > 0 else 0
                            lon = pts[1] if len(pts) > 1 else 0
                        return {"country": d.get("country", "Unknown"),
                                "cc": d.get("countryCode", "??"),
                                "region": d.get("regionName", d.get("region", "Unknown")),
                                "city": d.get("city", "Unknown"),
                                "zip": d.get("zip", d.get("postal", "N/A")),
                                "lat": lat, "lon": lon,
                                "tz": d.get("timezone", "Unknown"),
                                "isp": d.get("isp", d.get("org", "Unknown")),
                                "org": d.get("org", "Unknown"),
                                "asn": d.get("as", d.get("asn", "Unknown")),
                                "as_name": d.get("asname", "Unknown"),
                                "mobile": d.get("mobile", False),
                                "proxy": d.get("proxy", False),
                                "hosting": d.get("hosting", False)}
            except: continue
        return None

    @staticmethod
    def blacklist(ip):
        rev = ".".join(reversed(ip.split(".")))
        hits = []
        for bl in Engine.BLACKLISTS:
            try:
                socket.gethostbyname(rev + "." + bl)
                hits.append(bl)
            except socket.gaierror: pass
        return hits

    @staticmethod
    def tor_check(ip):
        rev = ".".join(reversed(ip.split(".")))
        try:
            socket.gethostbyname(rev + "." + Engine.TOR_DNSBL)
            return True
        except socket.gaierror: return False

    @staticmethod
    def whois(ip):
        try:
            r = subprocess.run(["whois", ip], capture_output=True, text=True, timeout=15,
                               creationflags=subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0)
            return r.stdout[:3000] if r.stdout else None
        except: return None

    @staticmethod
    def traceroute(ip, max_hops=20):
        if platform.system() == "Windows":
            cmd = ["tracert", "-d", "-h", str(max_hops), ip]
        else:
            cmd = ["traceroute", "-n", "-m", str(max_hops), ip]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=60,
                               creationflags=subprocess.CREATE_NO_WINDOW if platform.system() == "Windows" else 0)
            if r.stdout:
                lines = []
                for l in r.stdout.splitlines()[:max_hops + 5]:
                    l = l.strip()
                    if l and not l.startswith("traceroute") and not l.startswith("Tracing"):
                        lines.append(l)
                return lines if lines else None
        except: pass
        return None

    @staticmethod
    def threat_score(ip, geo_data=None, bl=None, tor=False):
        s = 0
        reasons = []
        if bl:
            c = len(bl)
            if c > 0:
                s += min(c * 12, 40)
                reasons.append("Listed on " + str(c) + " blacklist(s)")
        if tor:
            s += 30
            reasons.append("Tor exit node detected")
        cl = Engine.cloud(ip)
        if cl:
            s += 10
            reasons.append("Datacenter IP (" + cl + ")")
        if geo_data:
            if geo_data.get("proxy"):
                s += 20
                reasons.append("Proxy/VPN detected")
            if geo_data.get("hosting"):
                s += 10
                reasons.append("Hosting/datacenter")
            if geo_data.get("mobile"):
                s -= 5
        if Engine.is_private(ip):
            return {"score": 0, "level": "LOW", "reasons": ["Private/internal IP"]}
        s = max(0, min(100, s))
        if s <= 20: lv = "LOW"
        elif s <= 50: lv = "MODERATE"
        elif s <= 75: lv = "HIGH"
        else: lv = "CRITICAL"
        return {"score": s, "level": lv, "reasons": reasons or ["No threat indicators"]}

    @staticmethod
    def get_hostname(): return socket.gethostname()

    @staticmethod
    def get_fqdn(): return socket.getfqdn()

    @staticmethod
    def get_local_ip():
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except: return "127.0.0.1"

    @staticmethod
    def get_interfaces():
        try:
            if platform.system() == "Windows":
                r = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, timeout=10,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                r = subprocess.run(["ip", "addr", "show"], capture_output=True, text=True, timeout=10)
            return r.stdout if r.stdout else None
        except: return None

    @staticmethod
    def get_arp():
        try:
            if platform.system() == "Windows":
                r = subprocess.run(["arp", "-a"], capture_output=True, text=True, timeout=10,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                r = subprocess.run(["ip", "neigh", "show"], capture_output=True, text=True, timeout=10)
            if r.stdout:
                entries = []
                for line in r.stdout.splitlines():
                    line = line.strip()
                    if line and not line.startswith("Interface") and not line.startswith("---"):
                        entries.append(line)
                return entries if entries else None
        except: pass
        return None

    @staticmethod
    def get_routes():
        try:
            if platform.system() == "Windows":
                r = subprocess.run(["route", "print"], capture_output=True, text=True, timeout=10,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                r = subprocess.run(["ip", "route", "show"], capture_output=True, text=True, timeout=10)
            if r.stdout:
                entries = []
                for line in r.stdout.splitlines():
                    line = line.strip()
                    if line and ("default" in line.lower() or re.match(r'^\d', line)):
                        entries.append(line)
                return entries if entries else None
        except: pass
        return None

    @staticmethod
    def get_dns_resolvers():
        resolvers = []
        try:
            if platform.system() == "Windows":
                r = subprocess.run(["ipconfig", "/all"], capture_output=True, text=True, timeout=10,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
                if r.stdout:
                    for line in r.stdout.splitlines():
                        if "DNS" in line and ":" in line:
                            resolvers.append(line.strip())
            else:
                try:
                    with open("/etc/resolv.conf", "r") as f:
                        for line in f:
                            if line.startswith("nameserver"):
                                ns = line.split()[1] if len(line.split()) > 1 else ""
                                resolvers.append("nameserver " + ns)
                except: pass
        except: pass
        return resolvers if resolvers else None

    @staticmethod
    def ping_sweep(subnet_base):
        alive = []
        base = ".".join(subnet_base.split(".")[:3])
        for i in range(1, 255):
            target = base + "." + str(i)
            try:
                if platform.system() == "Windows":
                    r = subprocess.run(["ping", "-n", "1", "-w", "500", target],
                                       capture_output=True, text=True, timeout=2,
                                       creationflags=subprocess.CREATE_NO_WINDOW)
                else:
                    r = subprocess.run(["ping", "-c", "1", "-W", "1", target],
                                       capture_output=True, text=True, timeout=2)
                if r.returncode == 0:
                    alive.append(target)
            except: pass
        return alive

    # ─── NEW v3 FEATURES ───

    @staticmethod
    def mac_vendor(mac_addr):
        """Look up MAC address vendor from OUI database."""
        if not mac_addr:
            return "Unknown"
        clean = mac_addr.replace(":", "").replace("-", "").replace(".", "").upper()
        if len(clean) < 6:
            return "Unknown"
        oui = clean[:6]
        return MAC_VENDORS.get(oui, "Unknown Vendor")

    @staticmethod
    def os_fingerprint_ttl(ip):
        """OS fingerprinting via TTL analysis."""
        try:
            if platform.system() == "Windows":
                r = subprocess.run(["ping", "-n", "1", "-w", "1000", ip],
                                   capture_output=True, text=True, timeout=5,
                                   creationflags=subprocess.CREATE_NO_WINDOW)
            else:
                r = subprocess.run(["ping", "-c", "1", "-W", "1", ip],
                                   capture_output=True, text=True, timeout=5)
            if r.stdout:
                ttl_match = re.search(r'[Tt][Tt][Ll][=:]?\s*(\d+)', r.stdout)
                if ttl_match:
                    ttl = int(ttl_match.group(1))
                    if ttl <= 64:
                        return {"os": "Linux/Unix/macOS", "ttl": ttl, "confidence": "HIGH"}
                    elif ttl <= 128:
                        return {"os": "Windows", "ttl": ttl, "confidence": "HIGH"}
                    else:
                        return {"os": "Network Device/Solaris", "ttl": ttl, "confidence": "MEDIUM"}
        except: pass
        return {"os": "Unknown", "ttl": 0, "confidence": "NONE"}

    @staticmethod
    def detect_iot(open_ports):
        """Detect IoT/CCTV devices based on open port signatures."""
        iot_devices = []
        for port, info in open_ports.items():
            if port in IOT_SIGNATURES:
                sig = IOT_SIGNATURES[port]
                iot_devices.append({
                    "port": port,
                    "service": sig[0],
                    "device_type": sig[1],
                    "risk": sig[2],
                })
        return iot_devices

    @staticmethod
    def wifi_scan():
        """Scan WiFi networks (Linux only, requires root)."""
        networks = []
        if platform.system() != "Linux":
            return None
        try:
            r = subprocess.run(["iwlist", "wlan0", "scan"], capture_output=True, text=True, timeout=15)
            if r.stdout:
                current = {}
                for line in r.stdout.splitlines():
                    line = line.strip()
                    if "ESSID" in line:
                        ssid = re.search(r'ESSID:"([^"]*)"', line)
                        if ssid:
                            current["ssid"] = ssid.group(1)
                    elif "Address" in line:
                        addr = re.search(r'Address:\s*([0-9A-Fa-f:]+)', line)
                        if addr:
                            current["bssid"] = addr.group(1)
                    elif "Channel" in line:
                        ch = re.search(r'Channel:(\d+)', line)
                        if ch:
                            current["channel"] = ch.group(1)
                    elif "Signal level" in line:
                        sig = re.search(r'Signal level=(-?\d+)', line)
                        if sig:
                            current["signal"] = sig.group(1) + " dBm"
                    elif "Encryption key" in line:
                        if "on" in line.lower():
                            current["encryption"] = "Yes"
                        else:
                            current["encryption"] = "Open"
                        if current.get("ssid") or current.get("bssid"):
                            networks.append(dict(current))
                        current = {}
        except: pass
        return networks if networks else None

    @staticmethod
    def extract_ips_from_text(text):
        """Extract IP addresses from text/headers."""
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
        found = re.findall(ip_pattern, text)
        return [ip for ip in found if Engine.valid_ip(ip)]

    @staticmethod
    def extract_ips_from_email(text):
        """Extract IPs from email headers."""
        results = []
        for line in text.splitlines():
            if any(kw in line.lower() for kw in ["received:", "x-originating-ip:", "x-forwarded-for:"]):
                ips = Engine.extract_ips_from_text(line)
                for ip in ips:
                    results.append({"ip": ip, "header": line.strip()[:100]})
        return results

    @staticmethod
    def extract_exif(filepath):
        """Extract EXIF metadata from images (basic, no PIL dependency)."""
        try:
            with open(filepath, "rb") as f:
                data = f.read()
            results = {"file": os.path.basename(filepath), "size": len(data)}
            if data[:2] == b'\xff\xd8':
                results["type"] = "JPEG"
                pos = 2
                while pos < len(data) - 1:
                    if data[pos] != 0xFF:
                        break
                    marker = data[pos + 1]
                    if marker == 0xE1:
                        length = struct.unpack(">H", data[pos+2:pos+4])[0]
                        exif = data[pos+4:pos+2+length]
                        if exif[:4] == b'Exif':
                            results["exif_present"] = True
                            try:
                                gps_start = exif.find(b'GPS')
                                if gps_start > 0:
                                    results["gps_data"] = "GPS coordinates found"
                            except: pass
                        break
                    elif marker == 0xDA:
                        break
                    else:
                        if pos + 3 < len(data):
                            length = struct.unpack(">H", data[pos+2:pos+4])[0]
                            pos += 2 + length
                        else:
                            break
            elif data[:8] == b'\x89PNG\r\n\x1a\n':
                results["type"] = "PNG"
            else:
                results["type"] = "Unknown"
            return results
        except Exception as e:
            return {"error": str(e)}

    @staticmethod
    def hibp_check(email):
        """Check HaveIBBeenPwned for email breaches (free API)."""
        try:
            url = "https://haveibeenpwned.com/api/v3/breachedaccount/" + urllib.parse.quote(email)
            req = urllib.request.Request(url, headers={"User-Agent": "VIPER-EYE-Check", "hibp-api-key": ""})
            with urllib.request.urlopen(req, timeout=10) as resp:
                breaches = json.loads(resp.read().decode("utf-8"))
                return [{"name": b.get("Name", ""), "domain": b.get("Domain", ""),
                         "date": b.get("BreachDate", ""), "count": b.get("PwnCount", 0)} for b in breaches]
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return "CLEAN"
            return None
        except: return None

    @staticmethod
    def shodan_query(ip):
        """Query Shodan free API for IP data."""
        try:
            url = "https://internetdb.shodan.io/" + ip
            req = urllib.request.Request(url, headers={"User-Agent": "VIPER-EYE/3.0"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
                return data
        except: return None

    @staticmethod
    def generate_tracker_link(domain="example.com", path="/track"):
        """Generate tracking link with unique ID."""
        uid = hashlib.md5(str(time.time()).encode()).hexdigest()[:10]
        return {"link": "https://" + domain + path + "?id=" + uid, "id": uid, "created": datetime.datetime.now().isoformat()}

    @staticmethod
    def anomaly_detect(history):
        """Basic statistical anomaly detection on scan history."""
        if len(history) < 3:
            return {"status": "Insufficient data", "anomalies": []}
        scores = [h.get("threat", {}).get("score", 0) for h in history if h.get("threat")]
        if not scores:
            return {"status": "No threat data", "anomalies": []}
        mean = sum(scores) / len(scores)
        std = (sum((x - mean) ** 2 for x in scores) / len(scores)) ** 0.5 if len(scores) > 1 else 0
        anomalies = []
        for h in history:
            s = h.get("threat", {}).get("score", 0)
            if std > 0 and abs(s - mean) > 2 * std:
                anomalies.append({"ip": h.get("ip", ""), "score": s, "deviation": round(abs(s - mean) / std, 2)})
        return {"mean": round(mean, 2), "std": round(std, 2), "anomalies": anomalies}


# ════════════════════════════════════════════════════════════════
# DATABASE
# ════════════════════════════════════════════════════════════════

class Database:
    def __init__(self, path="viper_eye.db"):
        self.path = path
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS scans (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, ts TEXT, data TEXT, threat_score INTEGER, threat_level TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, first_seen TEXT, last_seen TEXT, visit_count INTEGER DEFAULT 1)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, type TEXT, message TEXT, severity TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY AUTOINCREMENT, uid TEXT, link TEXT, created TEXT, clicks INTEGER DEFAULT 0)")
        self.conn.commit()

    def save_scan(self, ip, data, threat_score, threat_level):
        self.conn.execute("INSERT INTO scans (ip, ts, data, threat_score, threat_level) VALUES (?,?,?,?,?)",
                          (ip, datetime.datetime.now().isoformat(), json.dumps(data, default=str), threat_score, threat_level))
        self.conn.commit()

    def track_session(self, ip):
        row = self.conn.execute("SELECT * FROM sessions WHERE ip=?", (ip,)).fetchone()
        if row:
            self.conn.execute("UPDATE sessions SET last_seen=?, visit_count=visit_count+1 WHERE ip=?",
                              (datetime.datetime.now().isoformat(), ip))
        else:
            self.conn.execute("INSERT INTO sessions (ip, first_seen, last_seen) VALUES (?,?,?)",
                              (ip, datetime.datetime.now().isoformat(), datetime.datetime.now().isoformat()))
        self.conn.commit()

    def get_sessions(self):
        return self.conn.execute("SELECT * FROM sessions ORDER BY last_seen DESC LIMIT 50").fetchall()

    def get_history(self, limit=50):
        return self.conn.execute("SELECT * FROM scans ORDER BY id DESC LIMIT ?", (limit,)).fetchall()

    def add_alert(self, atype, message, severity):
        self.conn.execute("INSERT INTO alerts (ts, type, message, severity) VALUES (?,?,?,?)",
                          (datetime.datetime.now().isoformat(), atype, message, severity))
        self.conn.commit()

    def get_alerts(self):
        return self.conn.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 50").fetchall()

    def save_link(self, uid, link):
        self.conn.execute("INSERT INTO links (uid, link, created) VALUES (?,?,?)",
                          (uid, link, datetime.datetime.now().isoformat()))
        self.conn.commit()

    def get_links(self):
        return self.conn.execute("SELECT * FROM links ORDER BY id DESC").fetchall()

    def get_scan_stats(self):
        total = self.conn.execute("SELECT COUNT(*) FROM scans").fetchone()[0]
        threats = self.conn.execute("SELECT COUNT(*) FROM scans WHERE threat_score > 50").fetchone()[0]
        return {"total": total, "threats": threats}

    def export_json(self):
        rows = self.conn.execute("SELECT * FROM scans").fetchall()
        return [{"id": r[0], "ip": r[1], "ts": r[2], "threat_score": r[4], "threat_level": r[5]} for r in rows]

    def export_csv(self):
        rows = self.conn.execute("SELECT * FROM scans").fetchall()
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["ID", "IP", "Timestamp", "Threat Score", "Threat Level"])
        for r in rows:
            writer.writerow([r[0], r[1], r[2], r[4], r[5]])
        return output.getvalue()


# ════════════════════════════════════════════════════════════════
# DISCORD WEBHOOK
# ════════════════════════════════════════════════════════════════

class DiscordAlert:
    WEBHOOK_URL = ""

    @staticmethod
    def set_webhook(url):
        DiscordAlert.WEBHOOK_URL = url

    @staticmethod
    def send(title, description, color=0x00ff88):
        if not DiscordAlert.WEBHOOK_URL:
            return False
        payload = {
            "username": "VIPER-EYE",
            "embeds": [{"title": title, "description": description, "color": color,
                        "timestamp": datetime.datetime.utcnow().isoformat()}]
        }
        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(DiscordAlert.WEBHOOK_URL, data=data,
                                          headers={"Content-Type": "application/json"})
            with urllib.request.urlopen(req, timeout=10) as resp:
                return resp.status in (200, 204)
        except: return False


# ════════════════════════════════════════════════════════════════
# GUI v3
# ════════════════════════════════════════════════════════════════

class ViperEye:

    def __init__(self, root):
        self.root = root
        self.root.title("VIPER-EYE // Ultimate IP Intelligence Suite v3.0")
        self.root.geometry("1420x900")
        self.root.minsize(1280, 800)
        self.root.configure(bg=C.VOID, cursor="crosshair")

        self.root.update_idletasks()
        sw = self.root.winfo_screenwidth()
        sh = self.root.winfo_screenheight()
        self.root.geometry("1420x900+" + str((sw-1420)//2) + "+" + str((sh-900)//2))

        self.scanning = False
        self.scan_thread = None
        self.last_results = {}
        self.scan_count = 0
        self.rain_chars = "01アイウエオカキクケコ<>{}[]|/\\"
        self.pulse_state = 0
        self.db = Database()
        self.scan_history = []

        self._fonts()
        self._styles()
        self._build()
        self._rain()
        self._pulse()
        self._graph_tick()

    def _fonts(self):
        self.f_title = tkfont.Font(family="Consolas", size=16, weight="bold")
        self.f_sub = tkfont.Font(family="Consolas", size=10, weight="bold")
        self.f_mono = tkfont.Font(family="Consolas", size=10)
        self.f_small = tkfont.Font(family="Consolas", size=9)
        self.f_input = tkfont.Font(family="Consolas", size=13, weight="bold")
        self.f_btn = tkfont.Font(family="Consolas", size=10, weight="bold")
        self.f_big = tkfont.Font(family="Consolas", size=32, weight="bold")
        self.f_rain = tkfont.Font(family="Consolas", size=9)

    def _styles(self):
        s = ttk.Style()
        s.theme_use("clam")
        s.configure("V.TNotebook", background=C.VOID, borderwidth=0)
        s.configure("V.TNotebook.Tab", background=C.PANEL, foreground=C.TXT2,
                     padding=[14, 6], font=self.f_small, borderwidth=0)
        s.map("V.TNotebook.Tab",
               background=[("selected", C.INPUT)],
               foreground=[("selected", C.GLOW_G)])

    def _build(self):
        self.main = tk.Frame(self.root, bg=C.VOID)
        self.main.pack(fill=tk.BOTH, expand=True, padx=6, pady=6)
        self._header()
        self._input_bar()
        content = tk.Frame(self.main, bg=C.VOID)
        content.pack(fill=tk.BOTH, expand=True, pady=(6, 0))
        self.nb = ttk.Notebook(content, style="V.TNotebook")
        self.nb.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 4))
        tabs = [
            ("OVERVIEW", self._tab_overview), ("NETWORK", self._tab_network),
            ("GEO", self._tab_geo), ("LOCAL", self._tab_local),
            ("PORTS", self._tab_ports), ("THREAT", self._tab_threat),
            ("IOT/CCTV", self._tab_iot), ("WHOIS", self._tab_whois),
            ("TRACE", self._tab_trace), ("TOOLS", self._tab_tools),
            ("DASHBOARD", self._tab_dashboard), ("RAW", self._tab_raw),
        ]
        self.texts = {}
        for name, builder in tabs:
            builder(name)
        self._side_panel(content)
        self._status_bar()

    def _header(self):
        hdr = tk.Frame(self.main, bg=C.VOID, height=55)
        hdr.pack(fill=tk.X, pady=(0, 2))
        hdr.pack_propagate(False)
        self.rain_cv = tk.Canvas(hdr, width=200, height=55, bg=C.VOID, highlightthickness=0)
        self.rain_cv.pack(side=tk.LEFT, padx=(0, 8))
        tf = tk.Frame(hdr, bg=C.VOID)
        tf.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        tk.Label(tf, text="VIPER-EYE", font=self.f_title, fg=C.GLOW_G, bg=C.VOID, anchor="w").pack(side=tk.LEFT)
        tk.Label(tf, text="  //  v3.0 ULTIMATE", font=self.f_mono, fg=C.TXT3, bg=C.VOID, anchor="w").pack(side=tk.LEFT)
        self.clock = tk.Label(hdr, text="", font=self.f_mono, fg=C.GLOW_C, bg=C.VOID)
        self.clock.pack(side=tk.RIGHT, padx=8)
        self._tick()

    def _input_bar(self):
        bar = tk.Frame(self.main, bg=C.PANEL, highlightbackground=C.BORDER, highlightthickness=1)
        bar.pack(fill=tk.X, pady=2, ipady=6)
        tk.Label(bar, text=" TARGET >", font=self.f_sub, fg=C.GLOW_R, bg=C.PANEL).pack(side=tk.LEFT, padx=(12, 6))
        self.entry = tk.Entry(bar, font=self.f_input, bg=C.INPUT, fg=C.GLOW_G,
                               insertbackground=C.GLOW_G, relief=tk.FLAT, width=28,
                               highlightthickness=2, highlightcolor=C.GLOW_G, highlightbackground=C.BORDER)
        self.entry.pack(side=tk.LEFT, padx=4, ipady=5)
        self.entry.bind("<Return>", lambda e: self._scan())
        self.btn_scan = tk.Button(bar, text="SCAN", font=self.f_btn, bg=C.GLOW_G, fg=C.VOID,
                                   activebackground=C.GLOW_C, relief=tk.FLAT, padx=18, pady=3, cursor="hand2", command=self._scan)
        self.btn_scan.pack(side=tk.LEFT, padx=8)
        self.btn_deep = tk.Button(bar, text="DEEP", font=self.f_btn, bg=C.GLOW_R, fg=C.GLOW_W,
                                   activebackground=C.GLOW_O, relief=tk.FLAT, padx=14, pady=3, cursor="hand2", command=self._deep)
        self.btn_deep.pack(side=tk.LEFT, padx=4)
        self.btn_local = tk.Button(bar, text="LOCAL", font=self.f_btn, bg=C.GLOW_P, fg=C.GLOW_W,
                                    activebackground=C.GLOW_PK, relief=tk.FLAT, padx=14, pady=3, cursor="hand2", command=self._local_scan)
        self.btn_local.pack(side=tk.LEFT, padx=4)
        self.btn_clear = tk.Button(bar, text="X CLR", font=self.f_btn, bg=C.INPUT, fg=C.TXT2,
                                    activebackground=C.CARD, relief=tk.FLAT, padx=10, pady=3, cursor="hand2", command=self._clear)
        self.btn_clear.pack(side=tk.LEFT, padx=4)
        self.btn_myip = tk.Button(bar, text="MY IP", font=self.f_btn, bg=C.INPUT, fg=C.GLOW_C,
                                   activebackground=C.CARD, relief=tk.FLAT, padx=10, pady=3, cursor="hand2", command=self._myip)
        self.btn_myip.pack(side=tk.RIGHT, padx=12)

    # ─── TAB BUILDERS ───

    def _make_text(self, parent):
        t = tk.Text(parent, font=self.f_mono, bg=C.DEEP, fg=C.TXT, insertbackground=C.GLOW_G,
                     relief=tk.FLAT, wrap=tk.WORD, padx=14, pady=10, state=tk.DISABLED,
                     cursor="arrow", selectbackground=C.GLOW_G, selectforeground=C.VOID, borderwidth=0)
        t.pack(fill=tk.BOTH, expand=True)
        return t

    def _tag(self, w, name, **kw):
        w.tag_configure(name, **kw)

    def _setup_tags(self, w):
        for n, c in [("t", C.GLOW_G), ("l", C.TXT2), ("v", C.TXT), ("d", C.GLOW_R),
                      ("s", C.GLOW_G), ("w", C.GLOW_O), ("i", C.GLOW_C), ("h", C.GLOW_P),
                      ("c", C.GLOW_Y), ("a", C.GLOW_PK), ("b", C.GLOW_P)]:
            self._tag(w, n, foreground=c)
        self._tag(w, "ts", foreground=C.GLOW_G, font=self.f_sub)
        self._tag(w, "hs", foreground=C.GLOW_P, font=self.f_sub)

    def _tab_overview(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_network(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_geo(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_local(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_ports(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_threat(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])
        self._tag(self.texts[name], "crits", foreground=C.GLOW_R, font=self.f_sub)
        self._tag(self.texts[name], "highs", foreground=C.GLOW_O, font=self.f_sub)
        self._tag(self.texts[name], "mods", foreground=C.GLOW_Y, font=self.f_sub)
        self._tag(self.texts[name], "lows", foreground=C.GLOW_G, font=self.f_sub)

    def _tab_iot(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_whois(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_trace(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")
        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_tools(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")

        btn_frame = tk.Frame(f, bg=C.DEEP)
        btn_frame.pack(fill=tk.X, padx=10, pady=5)

        tools = [
            ("LINK GEN", self._tool_linkgen), ("EMAIL EXTRACT", self._tool_email),
            ("EXIF EXTRACT", self._tool_exif), ("SHODAN LOOKUP", self._tool_shodan),
            ("DARK WEB CHECK", self._tool_hibp), ("EXPORT JSON", self._tool_export_json),
            ("EXPORT CSV", self._tool_export_csv), ("WIFI SCAN", self._tool_wifi),
            ("DISCORD SETUP", self._tool_discord), ("IP EXTRACTOR", self._tool_ip_extract),
        ]
        for i, (label, cmd) in enumerate(tools):
            r = i // 5
            c = i % 5
            btn = tk.Button(btn_frame, text=label, font=self.f_btn, bg=C.INPUT, fg=C.GLOW_C,
                             activebackground=C.CARD, relief=tk.FLAT, padx=8, pady=4, cursor="hand2", command=cmd)
            btn.grid(row=r, column=c, padx=3, pady=3, sticky="ew")

        for c in range(5):
            btn_frame.columnconfigure(c, weight=1)

        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_dashboard(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  " + name + "  ")

        # Graph canvas
        self.graph_cv = tk.Canvas(f, bg=C.DEEP, highlightthickness=0, height=180)
        self.graph_cv.pack(fill=tk.X, padx=10, pady=(5, 0))

        self.texts[name] = self._make_text(f)
        self._setup_tags(self.texts[name])

    def _tab_raw(self, name):
        f = tk.Frame(self.nb, bg=C.DEEP)
        self.nb.add(f, text="  { }  ")
        self.texts[name] = self._make_text(f)

    # ─── SIDE PANEL ───

    def _side_panel(self, parent):
        p = tk.Frame(parent, bg=C.PANEL, width=260, highlightbackground=C.BORDER, highlightthickness=1)
        p.pack(side=tk.RIGHT, fill=tk.Y, padx=(4, 0))
        p.pack_propagate(False)

        tk.Label(p, text="=" * 32, font=self.f_small, fg=C.DIM, bg=C.PANEL).pack(pady=(8, 0))
        tk.Label(p, text="THREAT INDEX", font=self.f_sub, fg=C.GLOW_R, bg=C.PANEL).pack(pady=(4, 2))
        self.thr_score = tk.Label(p, text="--", font=self.f_big, fg=C.TXT3, bg=C.PANEL)
        self.thr_score.pack(pady=4)
        self.thr_level = tk.Label(p, text="NO DATA", font=self.f_sub, fg=C.TXT3, bg=C.PANEL)
        self.thr_level.pack(pady=(0, 6))
        self.thr_cv = tk.Canvas(p, width=220, height=18, bg=C.ABYSS, highlightthickness=0)
        self.thr_cv.pack(pady=(0, 8))
        tk.Label(p, text="=" * 32, font=self.f_small, fg=C.DIM, bg=C.PANEL).pack()

        tk.Label(p, text="QUICK READ", font=self.f_sub, fg=C.GLOW_C, bg=C.PANEL).pack(pady=(8, 4))
        self.qi = {}
        for k in ["IP", "Type", "Country", "City", "ISP", "Cloud", "Proxy", "Tor", "Ports", "OS", "IoT"]:
            row = tk.Frame(p, bg=C.PANEL)
            row.pack(fill=tk.X, padx=14, pady=1)
            tk.Label(row, text=k + ":", font=self.f_small, fg=C.TXT3, bg=C.PANEL, anchor="w").pack(side=tk.LEFT)
            v = tk.Label(row, text="--", font=self.f_small, fg=C.TXT, bg=C.PANEL, anchor="e")
            v.pack(side=tk.RIGHT)
            self.qi[k] = v

        tk.Label(p, text="=" * 32, font=self.f_small, fg=C.DIM, bg=C.PANEL).pack(pady=(8, 4))
        tk.Label(p, text="HISTORY", font=self.f_sub, fg=C.GLOW_P, bg=C.PANEL).pack(pady=(4, 4))
        self.hist = tk.Listbox(p, font=self.f_small, bg=C.INPUT, fg=C.TXT,
                                selectbackground=C.GLOW_G, selectforeground=C.VOID,
                                relief=tk.FLAT, height=8, highlightthickness=0)
        self.hist.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        self.hist.bind("<<ListboxSelect>>", self._hist_sel)

    # ─── STATUS BAR ───

    def _status_bar(self):
        sb = tk.Frame(self.main, bg=C.PANEL, height=22, highlightbackground=C.BORDER, highlightthickness=1)
        sb.pack(fill=tk.X, pady=(4, 0), ipady=2)
        self.stat = tk.Label(sb, text="READY", font=self.f_small, fg=C.GLOW_G, bg=C.PANEL, anchor="w")
        self.stat.pack(side=tk.LEFT, padx=10)
        self.prog = tk.Label(sb, text="", font=self.f_small, fg=C.TXT2, bg=C.PANEL, anchor="e")
        self.prog.pack(side=tk.RIGHT, padx=10)
        self.cnt = tk.Label(sb, text="Scans: 0 | DB: 0", font=self.f_small, fg=C.TXT3, bg=C.PANEL)
        self.cnt.pack(side=tk.RIGHT, padx=10)

    # ─── ANIMATIONS ───

    def _tick(self):
        self.clock.config(text=datetime.datetime.now().strftime("%H:%M:%S"))
        self.root.after(1000, self._tick)

    def _rain(self):
        self.rain_cv.delete("all")
        for _ in range(30):
            x = random.randint(0, 200)
            y = random.randint(0, 55)
            ch = random.choice(self.rain_chars)
            col = random.choice([C.GLOW_G, "#003311", "#005522", C.GLOW_C, "#001a33"])
            self.rain_cv.create_text(x, y, text=ch, fill=col, font=self.f_rain)
        self.root.after(100, self._rain)

    def _pulse(self):
        if self.scanning:
            colors = [C.GLOW_G, C.GLOW_C, C.GLOW_Y, C.GLOW_O]
            self.pulse_state = (self.pulse_state + 1) % len(colors)
            self.btn_scan.config(bg=colors[self.pulse_state])
        self.root.after(180, self._pulse)

    def _graph_tick(self):
        """Update dashboard graph periodically."""
        try:
            self._draw_graph()
        except: pass
        self.root.after(3000, self._graph_tick)

    def _draw_graph(self):
        cv = self.graph_cv
        cv.delete("all")
        w = cv.winfo_width()
        h = 180
        if w < 10: w = 800

        cv.create_text(w // 2, 12, text="THREAT SCORE HISTORY", fill=C.TXT3, font=self.f_small)
        cv.create_line(20, h - 20, w - 20, h - 20, fill=C.DIM, width=1)
        cv.create_line(20, 25, 20, h - 20, fill=C.DIM, width=1)

        for i in range(0, 101, 25):
            y = h - 20 - (i / 100) * (h - 50)
            cv.create_text(12, y, text=str(i), fill=C.TXT3, font=("Consolas", 7))
            cv.create_line(20, y, w - 20, y, fill="#111122", width=1)

        history = self.scan_history[-30:]
        if len(history) > 1:
            points = []
            step = (w - 60) / max(len(history) - 1, 1)
            for idx, h_data in enumerate(history):
                x = 30 + idx * step
                score = h_data.get("threat", {}).get("score", 0)
                y = h - 20 - (score / 100) * (h - 50)
                points.append((x, y))

            for i in range(len(points) - 1):
                s = history[i].get("threat", {}).get("score", 0)
                col = C.GLOW_G if s <= 20 else C.GLOW_Y if s <= 50 else C.GLOW_O if s <= 75 else C.GLOW_R
                cv.create_line(points[i][0], points[i][1], points[i+1][0], points[i+1][1], fill=col, width=2)

            for i, (x, y) in enumerate(points):
                s = history[i].get("threat", {}).get("score", 0)
                col = C.GLOW_G if s <= 20 else C.GLOW_Y if s <= 50 else C.GLOW_O if s <= 75 else C.GLOW_R
                cv.create_oval(x-3, y-3, x+3, y+3, fill=col, outline="")

    # ─── TEXT HELPERS ───

    def _clr(self, w):
        w.config(state=tk.NORMAL); w.delete("1.0", tk.END); w.config(state=tk.DISABLED)

    def _w(self, w, text, tag=None):
        w.config(state=tk.NORMAL)
        if tag: w.insert(tk.END, text, tag)
        else: w.insert(tk.END, text)
        w.config(state=tk.DISABLED)

    def _stat(self, text, color=C.GLOW_G): self.stat.config(text=text, fg=color)
    def _prog(self, text): self.prog.config(text=text)

    def _update_db_counter(self):
        stats = self.db.get_scan_stats()
        self.cnt.config(text="Scans: " + str(self.scan_count) + " | DB: " + str(stats["total"]))

    # ─── TOOLS ───

    def _tool_linkgen(self):
        t = self.texts["TOOLS"]
        self._clr(t)
        link = Engine.generate_tracker_link()
        self.db.save_link(link["id"], link["link"])
        self._w(t, "\n  TRACKING LINK GENERATED\n\n", "ts")
        self._w(t, "  Link:  ", "l")
        self._w(t, link["link"] + "\n", "i")
        self._w(t, "  ID:    ", "l")
        self._w(t, link["id"] + "\n", "v")
        self._w(t, "  Time:  ", "l")
        self._w(t, link["created"] + "\n\n", "v")
        self._w(t, "  Deploy this link to track visitors.\n", "l")

    def _tool_email(self):
        win = tk.Toplevel(self.root)
        win.title("Email Header IP Extractor")
        win.geometry("600x400")
        win.configure(bg=C.VOID)
        tk.Label(win, text="Paste email headers:", font=self.f_sub, fg=C.GLOW_C, bg=C.VOID).pack(pady=5)
        txt = tk.Text(win, font=self.f_small, bg=C.INPUT, fg=C.TXT, height=12)
        txt.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        def extract():
            text = txt.get("1.0", tk.END)
            results = Engine.extract_ips_from_email(text)
            if results:
                txt.delete("1.0", tk.END)
                for r in results:
                    txt.insert(tk.END, "IP: " + r["ip"] + " | " + r["header"] + "\n")
            else:
                txt.delete("1.0", tk.END)
                txt.insert(tk.END, "No IPs found in headers.")
        tk.Button(win, text="EXTRACT", font=self.f_btn, bg=C.GLOW_C, fg=C.VOID,
                  relief=tk.FLAT, command=extract).pack(pady=5)

    def _tool_exif(self):
        filepath = filedialog.askopenfilename(title="Select file for EXIF extraction",
                                                filetypes=[("Images", "*.jpg *.jpeg *.png *.gif"), ("All", "*.*")])
        if filepath:
            t = self.texts["TOOLS"]
            self._clr(t)
            result = Engine.extract_exif(filepath)
            self._w(t, "\n  FILE METADATA EXTRACTION\n\n", "ts")
            for k, v in result.items():
                self._w(t, "  " + k + ": ", "l")
                self._w(t, str(v) + "\n", "v")

    def _tool_shodan(self):
        target = self.entry.get().strip()
        if not target or not Engine.valid_ip(target):
            messagebox.showwarning("No Target", "Enter a valid IP first.")
            return
        t = self.texts["TOOLS"]
        self._clr(t)
        self._w(t, "\n  SHODAN INTERNETDB LOOKUP\n\n", "ts")
        self._w(t, "  Querying Shodan for " + target + "...\n\n", "i")
        data = Engine.shodan_query(target)
        if data:
            for k, v in data.items():
                self._w(t, "  " + str(k) + ": ", "l")
                self._w(t, str(v) + "\n", "v")
        else:
            self._w(t, "  No Shodan data found or API limit reached.\n", "l")

    def _tool_hibp(self):
        win = tk.Toplevel(self.root)
        win.title("Dark Web Exposure Check (HIBP)")
        win.geometry("500x200")
        win.configure(bg=C.VOID)
        tk.Label(win, text="Enter email to check:", font=self.f_sub, fg=C.GLOW_R, bg=C.VOID).pack(pady=10)
        entry = tk.Entry(win, font=self.f_input, bg=C.INPUT, fg=C.GLOW_G, width=35)
        entry.pack(pady=5)
        def check():
            email = entry.get().strip()
            if not email: return
            t = self.texts["TOOLS"]
            self._clr(t)
            self._w(t, "\n  DARK WEB EXPOSURE CHECK\n\n", "ts")
            self._w(t, "  Checking " + email + "...\n\n", "i")
            result = Engine.hibp_check(email)
            if result == "CLEAN":
                self._w(t, "  [OK] No breaches found.\n", "s")
            elif result:
                self._w(t, "  [!] BREACHES FOUND:\n\n", "d")
                for b in result[:20]:
                    self._w(t, "  " + b.get("name", "") + " (" + b.get("date", "") + ") - " + str(b.get("count", 0)) + " records\n", "w")
            else:
                self._w(t, "  Could not check (API rate limit).\n", "l")
        tk.Button(win, text="CHECK", font=self.f_btn, bg=C.GLOW_R, fg=C.GLOW_W,
                  relief=tk.FLAT, command=check).pack(pady=10)

    def _tool_export_json(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON", "*.json")])
        if filepath:
            data = self.db.export_json()
            with open(filepath, "w") as f:
                json.dump(data, f, indent=2)
            messagebox.showinfo("Exported", "JSON saved to " + filepath)

    def _tool_export_csv(self):
        filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV", "*.csv")])
        if filepath:
            csv_data = self.db.export_csv()
            with open(filepath, "w") as f:
                f.write(csv_data)
            messagebox.showinfo("Exported", "CSV saved to " + filepath)

    def _tool_wifi(self):
        t = self.texts["TOOLS"]
        self._clr(t)
        self._w(t, "\n  WIFI NETWORK SCAN\n\n", "ts")
        if platform.system() != "Linux":
            self._w(t, "  WiFi scanning requires Linux (iwlist).\n", "w")
            self._w(t, "  Showing available interfaces instead...\n\n", "l")
            ifs = Engine.get_interfaces()
            if ifs:
                for line in str(ifs).splitlines()[:30]:
                    if "wireless" in line.lower() or "wlan" in line.lower() or "wifi" in line.lower():
                        self._w(t, "  " + line.strip() + "\n", "v")
            return
        self._w(t, "  Scanning (requires root)...\n\n", "i")
        networks = Engine.wifi_scan()
        if networks:
            for n in networks[:30]:
                ssid = n.get("ssid", "Hidden")
                bssid = n.get("bssid", "Unknown")
                sig = n.get("signal", "N/A")
                enc = n.get("encryption", "Unknown")
                ch = n.get("channel", "N/A")
                self._w(t, "  " + ssid + " | ", "v")
                self._w(t, bssid + " | ", "l")
                self._w(t, sig + " | ", "i")
                self._w(t, "Ch:" + ch + " | ", "l")
                self._w(t, enc + "\n", "d" if enc == "Open" else "s")
        else:
            self._w(t, "  No networks found (need root + wlan0).\n", "l")

    def _tool_discord(self):
        win = tk.Toplevel(self.root)
        win.title("Discord Webhook Setup")
        win.geometry("550x150")
        win.configure(bg=C.VOID)
        tk.Label(win, text="Discord Webhook URL:", font=self.f_sub, fg=C.GLOW_P, bg=C.VOID).pack(pady=5)
        entry = tk.Entry(win, font=self.f_mono, bg=C.INPUT, fg=C.GLOW_G, width=60)
        entry.pack(pady=5)
        def save():
            DiscordAlert.set_webhook(entry.get().strip())
            messagebox.showinfo("Saved", "Webhook configured!")
            win.destroy()
        tk.Button(win, text="SAVE", font=self.f_btn, bg=C.GLOW_P, fg=C.GLOW_W,
                  relief=tk.FLAT, command=save).pack(pady=5)

    def _tool_ip_extract(self):
        win = tk.Toplevel(self.root)
        win.title("IP Extractor from Text")
        win.geometry("600x400")
        win.configure(bg=C.VOID)
        tk.Label(win, text="Paste text to extract IPs:", font=self.f_sub, fg=C.GLOW_C, bg=C.VOID).pack(pady=5)
        txt = tk.Text(win, font=self.f_small, bg=C.INPUT, fg=C.TXT, height=12)
        txt.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        def extract():
            text = txt.get("1.0", tk.END)
            ips = Engine.extract_ips_from_text(text)
            if ips:
                txt.delete("1.0", tk.END)
                for ip in set(ips):
                    txt.insert(tk.END, ip + "\n")
            else:
                txt.delete("1.0", tk.END)
                txt.insert(tk.END, "No IPs found.")
        tk.Button(win, text="EXTRACT", font=self.f_btn, bg=C.GLOW_C, fg=C.VOID,
                  relief=tk.FLAT, command=extract).pack(pady=5)

    # ─── SCANNING ───

    def _scan(self): self._do_scan(False)
    def _deep(self): self._do_scan(True)

    def _local_scan(self):
        lip = Engine.get_local_ip()
        self.entry.delete(0, tk.END)
        self.entry.insert(0, lip)
        self._do_scan(True)

    def _myip(self):
        self._stat("Detecting public IP...", C.GLOW_C)
        try:
            req = urllib.request.Request("https://api.ipify.org?format=json",
                                          headers={"User-Agent": "VIPER-EYE/3.0"})
            with urllib.request.urlopen(req, timeout=5) as resp:
                d = json.loads(resp.read())
                ip = d.get("ip", "")
                if ip:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0, ip)
                    self._scan()
                else: self._stat("IP detection failed", C.GLOW_R)
        except: self._stat("IP detection failed", C.GLOW_R)

    def _do_scan(self, deep):
        target = self.entry.get().strip()
        if not target:
            messagebox.showwarning("No Target", "Enter an IP or domain.")
            return
        if not Engine.valid_ip(target):
            resolved = Engine.resolve(target)
            if resolved:
                target = resolved
                self.entry.delete(0, tk.END)
                self.entry.insert(0, target)
            else:
                messagebox.showerror("Failed", "Could not resolve: " + target)
                return
        if self.scanning: return

        self.scanning = True
        mode = "DEEP" if deep else "QUICK"
        self._stat("[" + mode + "] SCANNING...", C.GLOW_Y)
        self._prog("Initializing...")

        for w in self.texts.values():
            self._clr(w)

        self.scan_thread = threading.Thread(target=self._run, args=(target, deep), daemon=True)
        self.scan_thread.start()

    def _run(self, ip, deep):
        R = {"ip": ip, "ts": datetime.datetime.now().isoformat(), "deep": deep}
        t0 = time.time()
        W = 48
        H = "-" * W
        priv = Engine.is_private(ip)

        # Phase 1 - Basic
        self.root.after(0, self._prog, "Phase 1/9 - Basic Intelligence...")
        R["private"] = priv
        R["class"] = Engine.ip_class(ip)
        R["binary"] = Engine.binary(ip)
        R["hex"] = Engine.hexip(ip)
        R["octal"] = Engine.octal(ip)
        R["integer"] = Engine.integer(ip)
        R["md5"] = hashlib.md5(ip.encode()).hexdigest()
        R["sha1"] = hashlib.sha1(ip.encode()).hexdigest()
        R["sha256"] = hashlib.sha256(ip.encode()).hexdigest()
        R["rdns"] = Engine.rev_dns(ip)
        R["hostname"] = Engine.get_hostname()
        R["fqdn"] = Engine.get_fqdn()
        R["local_ip"] = Engine.get_local_ip()

        # Phase 2 - Network
        self.root.after(0, self._prog, "Phase 2/9 - Network Analysis...")
        R["cloud"] = Engine.cloud(ip)
        subnets = {}
        for cidr in [8, 16, 24, 28, 30, 32]:
            try: subnets[cidr] = Engine.subnet(ip, cidr)
            except: pass
        R["subnets"] = subnets

        # Phase 3 - Geo
        self.root.after(0, self._prog, "Phase 3/9 - Geolocation...")
        R["geo"] = Engine.geo(ip)

        # Phase 4 - Local
        self.root.after(0, self._prog, "Phase 4/9 - Local Intelligence...")
        if priv:
            R["interfaces"] = Engine.get_interfaces()
            R["arp"] = Engine.get_arp()
            R["routes"] = Engine.get_routes()
            R["dns_resolvers"] = Engine.get_dns_resolvers()
            if deep:
                self.root.after(0, self._prog, "Phase 4/9 - Ping Sweep...")
                R["alive_hosts"] = Engine.ping_sweep(ip)
            else: R["alive_hosts"] = None
        else:
            R["interfaces"] = None; R["arp"] = None; R["routes"] = None
            R["dns_resolvers"] = None; R["alive_hosts"] = None

        # Phase 5 - Ports
        self.root.after(0, self._prog, "Phase 5/9 - Port Scanning...")
        ports_list = list(Engine.PORTS.keys())
        if deep:
            ports_list += [1080, 1723, 2049, 2121, 2222, 3128, 4443, 5000,
                           5555, 6000, 6443, 7001, 7777, 8081, 8181, 9000,
                           9090, 9200, 9443, 10000, 10443, 11211, 5353, 1900]
        open_p = {}
        total = len(ports_list)
        for idx, p in enumerate(ports_list):
            if idx % 3 == 0:
                self.root.after(0, self._prog, "Phase 5/9 - Port " + str(p) + " (" + str(idx+1) + "/" + str(total) + ")...")
            if Engine.scan_port(ip, p, timeout=1.0 if not deep else 2.0):
                si = Engine.PORTS.get(p, ("Unknown", "Unknown Service"))
                b = Engine.banner(ip, p) if deep else None
                open_p[p] = {"svc": si[0], "desc": si[1], "banner": b}
        R["open_ports"] = open_p

        # Phase 6 - OS Fingerprint
        self.root.after(0, self._prog, "Phase 6/9 - OS Fingerprinting...")
        R["os_fp"] = Engine.os_fingerprint_ttl(ip)

        # Phase 7 - IoT Detection
        self.root.after(0, self._prog, "Phase 7/9 - IoT/CCTV Detection...")
        R["iot"] = Engine.detect_iot(open_p)

        # Phase 8 - Threat
        self.root.after(0, self._prog, "Phase 8/9 - Threat Analysis...")
        R["blacklist"] = Engine.blacklist(ip)
        R["tor"] = Engine.tor_check(ip)
        R["threat"] = Engine.threat_score(ip, R.get("geo"), R["blacklist"], R["tor"])

        # Phase 9 - WHOIS/Trace
        self.root.after(0, self._prog, "Phase 9/9 - WHOIS & Trace...")
        if deep and not priv:
            R["whois"] = Engine.whois(ip)
        else: R["whois"] = None
        if deep:
            R["trace"] = Engine.traceroute(ip)
        else: R["trace"] = None

        # Shodan (quick, no auth)
        if not priv:
            R["shodan"] = Engine.shodan_query(ip)
        else:
            R["shodan"] = None

        elapsed = time.time() - t0
        R["time"] = round(elapsed, 2)
        self.last_results = R
        self.scan_count += 1
        self.scan_history.append(R)

        # Save to DB
        th = R.get("threat", {})
        self.db.save_scan(ip, R, th.get("score", 0), th.get("level", "UNKNOWN"))
        self.db.track_session(ip)

        # Discord alert for high threats
        if th.get("score", 0) >= 50:
            self.db.add_alert("HIGH_THREAT", ip + " scored " + str(th.get("score", 0)), "HIGH")
            DiscordAlert.send("HIGH THREAT DETECTED", ip + " | Score: " + str(th.get("score", 0)) + " | Level: " + th.get("level", ""), 0xff0044)

        # IoT alerts
        if R.get("iot"):
            self.db.add_alert("IOT_FOUND", ip + " has " + str(len(R["iot"])) + " IoT device signatures", "MEDIUM")
            DiscordAlert.send("IoT DEVICE DETECTED", ip + " | Devices: " + str(len(R["iot"])), 0xff8800)

        self.root.after(0, self._populate, R, deep)
        self.root.after(0, self._done, ip, elapsed)

    def _done(self, ip, elapsed):
        self.scanning = False
        self.btn_scan.config(bg=C.GLOW_G)
        self._stat("COMPLETE // " + ip, C.GLOW_G)
        self._prog("Done in " + str(round(elapsed, 1)) + "s")
        self._update_db_counter()
        ts = datetime.datetime.now().strftime("%H:%M:%S")
        self.hist.insert(0, "[" + ts + "] " + ip)

    # ─── POPULATE ───

    def _populate(self, R, deep):
        ip = R["ip"]
        W = 48
        H = "-" * W
        priv = R.get("private", False)

        # ═══ OVERVIEW ═══
        t = self.texts["OVERVIEW"]
        self._clr(t)
        self._w(t, "\n  +" + H + "+\n", "ts")
        self._w(t, "  |  TARGET INTELLIGENCE REPORT                   |\n", "ts")
        self._w(t, "  +" + H + "+\n\n", "ts")

        self._w(t, "  +- IP IDENTITY " + "-" * 33 + "+\n", "hs")
        self._w(t, "  |  Address:     ", "l"); self._w(t, ip + "\n", "v")
        self._w(t, "  |  Type:        ", "l")
        self._w(t, ("PRIVATE" if priv else "PUBLIC") + "\n", "s" if priv else "w")
        self._w(t, "  |  Class:       ", "l"); self._w(t, R["class"] + "\n", "v")
        self._w(t, "  |  Reverse DNS: ", "l")
        self._w(t, (R.get("rdns") or "None") + "\n", "i")
        self._w(t, "  |  Hostname:    ", "l"); self._w(t, R.get("hostname", "N/A") + "\n", "v")
        self._w(t, "  |  FQDN:        ", "l"); self._w(t, R.get("fqdn", "N/A") + "\n", "v")
        self._w(t, "  |  Local IP:    ", "l"); self._w(t, R.get("local_ip", "N/A") + "\n", "i")

        os_fp = R.get("os_fp", {})
        self._w(t, "  |  OS Guess:    ", "l")
        self._w(t, os_fp.get("os", "Unknown") + " (TTL:" + str(os_fp.get("ttl", 0)) + ")\n", "c")

        self._w(t, "  +" + H + "+\n\n", "hs")

        self._w(t, "  +- REPRESENTATIONS " + "-" * 30 + "+\n", "hs")
        self._w(t, "  |  Binary:  ", "l"); self._w(t, R["binary"] + "\n", "v")
        self._w(t, "  |  Hex:     ", "l"); self._w(t, "0x" + R["hex"] + "\n", "v")
        self._w(t, "  |  Octal:   ", "l"); self._w(t, R["octal"] + "\n", "v")
        self._w(t, "  |  Integer: ", "l"); self._w(t, format(R["integer"], ",") + "\n", "v")
        self._w(t, "  +" + H + "+\n\n", "hs")

        self._w(t, "  +- HASH FINGERPRINTS " + "-" * 28 + "+\n", "hs")
        self._w(t, "  |  MD5:    ", "l"); self._w(t, R["md5"] + "\n", "v")
        self._w(t, "  |  SHA1:   ", "l"); self._w(t, R["sha1"] + "\n", "v")
        self._w(t, "  |  SHA256: ", "l"); self._w(t, R["sha256"] + "\n", "v")
        self._w(t, "  +" + H + "+\n", "hs")

        # ═══ NETWORK ═══
        t = self.texts["NETWORK"]
        self._clr(t)
        self._w(t, "\n  +" + H + "+\n", "ts")
        self._w(t, "  |  NETWORK INTELLIGENCE                         |\n", "ts")
        self._w(t, "  +" + H + "+\n\n", "ts")
        cl = R.get("cloud")
        if cl:
            self._w(t, "  CLOUD: ", "l"); self._w(t, cl + "\n\n", "s")
        for cidr, info in R.get("subnets", {}).items():
            self._w(t, "  +- /" + str(cidr) + " " + "-" * 38 + "+\n", "ts")
            for k in ["network", "broadcast", "mask", "wildcard", "first", "last"]:
                self._w(t, "  |  " + k + ": ", "l"); self._w(t, str(info[k]) + "\n", "v")
            self._w(t, "  |  hosts: ", "l"); self._w(t, format(info["hosts"], ",") + "\n", "v")
            self._w(t, "  +" + H + "+\n\n", "ts")

        # ═══ GEO ═══
        t = self.texts["GEO"]
        self._clr(t)
        geo = R.get("geo")
        if geo:
            self._w(t, "\n  +" + H + "+\n", "ts")
            self._w(t, "  |  GEOLOCATION                                  |\n", "ts")
            self._w(t, "  +" + H + "+\n\n", "ts")
            self._w(t, "  Country:  ", "l"); self._w(t, str(geo.get("country","")) + " (" + str(geo.get("cc","")) + ")\n", "v")
            self._w(t, "  Region:   ", "l"); self._w(t, str(geo.get("region","")) + "\n", "v")
            self._w(t, "  City:     ", "l"); self._w(t, str(geo.get("city","")) + "\n", "v")
            self._w(t, "  Timezone: ", "l"); self._w(t, str(geo.get("tz","")) + "\n\n", "v")
            lat = geo.get("lat", 0); lon = geo.get("lon", 0)
            self._w(t, "  Lat: ", "l"); self._w(t, str(lat) + "\n", "c")
            self._w(t, "  Lon: ", "l"); self._w(t, str(lon) + "\n", "c")
            self._w(t, "  Map: ", "l"); self._w(t, "https://maps.google.com/?q=" + str(lat) + "," + str(lon) + "\n\n", "i")
            self._w(t, "  ISP: ", "l"); self._w(t, str(geo.get("isp","")) + "\n", "v")
            self._w(t, "  Org: ", "l"); self._w(t, str(geo.get("org","")) + "\n", "v")
            self._w(t, "  ASN: ", "l"); self._w(t, str(geo.get("asn","")) + "\n\n", "v")
            flags = []
            if geo.get("mobile"): flags.append("MOBILE")
            if geo.get("proxy"): flags.append("PROXY/VPN")
            if geo.get("hosting"): flags.append("HOSTING")
            if flags:
                self._w(t, "  FLAGS: ", "l"); self._w(t, " | ".join(flags) + "\n", "w")
        elif priv:
            self._w(t, "\n  PRIVATE NETWORK GEOLOGY\n\n", "ts")
            octets = ip.split(".")
            first = int(octets[0]); second = int(octets[1])
            if first == 10:
                rfc = "Class A /8 (RFC 1918) - Large enterprise, VPN, VPC"
            elif first == 172 and 16 <= second <= 31:
                rfc = "Class B /12 (RFC 1918) - Medium networks"
            elif first == 192 and second == 168:
                rfc = "Class C /16 (RFC 1918) - Home/SOHO"
            elif first == 127:
                rfc = "Loopback (RFC 1122) - Localhost"
            else:
                rfc = "Other reserved"
            self._w(t, "  RFC Class: ", "l"); self._w(t, rfc + "\n\n", "c")
            # Gateway prediction
            if first == 192 and second == 168:
                gws = ["192.168." + octets[2] + ".1", "192.168." + octets[2] + ".254"]
            elif first == 10:
                gws = ["10." + octets[1] + "." + octets[2] + ".1"]
            else:
                gws = []
            if gws:
                self._w(t, "  Likely Gateways:\n", "l")
                for gw in gws:
                    self._w(t, "    -> ", "l"); self._w(t, gw + "\n", "c")
            # ARP
            arp = R.get("arp")
            if arp:
                self._w(t, "\n  NEIGHBOR DEVICES (" + str(len(arp)) + "):\n", "ts")
                for entry in arp[:20]:
                    self._w(t, "  " + entry + "\n", "v")
            # DNS
            dns = R.get("dns_resolvers")
            if dns:
                self._w(t, "\n  DNS RESOLVERS:\n", "ts")
                for d in dns[:10]:
                    self._w(t, "  " + d + "\n", "i")
            # Alive
            alive = R.get("alive_hosts")
            if alive:
                self._w(t, "\n  ALIVE HOSTS (" + str(len(alive)) + "):\n", "ts")
                for h in alive:
                    self._w(t, "  [+] " + h + "\n", "s")
            elif R.get("alive_hosts") is None and not deep:
                self._w(t, "\n  [i] DEEP SCAN for host discovery\n", "i")
        else:
            self._w(t, "\n  No geolocation data.\n", "l")

        # ═══ LOCAL ═══
        t = self.texts["LOCAL"]
        self._clr(t)
        if priv:
            self._w(t, "\n  LOCAL NETWORK INTELLIGENCE\n\n", "ts")
            ifs = R.get("interfaces")
            if ifs:
                self._w(t, "  +- INTERFACES " + "-" * 34 + "+\n", "ts")
                for line in str(ifs).splitlines()[:50]:
                    if line.strip():
                        self._w(t, "  " + line.strip() + "\n", "v")
                self._w(t, "  +" + H + "+\n\n", "ts")
            routes = R.get("routes")
            if routes:
                self._w(t, "  +- ROUTES " + "-" * 38 + "+\n", "ts")
                for r in routes[:20]:
                    self._w(t, "  " + r + "\n", "v")
                self._w(t, "  +" + H + "+\n", "ts")
            # MAC vendor lookup from ARP
            arp = R.get("arp")
            if arp:
                self._w(t, "\n  +- MAC VENDOR LOOKUP " + "-" * 26 + "+\n", "ts")
                for entry in arp[:30]:
                    # Try to extract MAC
                    mac_match = re.search(r'([0-9A-Fa-f]{2}[:-]){5}[0-9A-Fa-f]{2}', entry)
                    if mac_match:
                        mac = mac_match.group(0)
                        vendor = Engine.mac_vendor(mac)
                        self._w(t, "  " + mac + " -> ", "l")
                        self._w(t, vendor + "\n", "i" if vendor != "Unknown Vendor" else "l")
        else:
            self._w(t, "\n  For private IPs only. Scan a 192.168.x.x address.\n", "l")

        # ═══ PORTS ═══
        t = self.texts["PORTS"]
        self._clr(t)
        op = R.get("open_ports", {})
        self._w(t, "\n  PORT SCAN RESULTS\n\n", "ts")
        if op:
            self._w(t, "  " + str(len(op)) + " OPEN PORT(S)\n\n", "s")
            for port, info in sorted(op.items()):
                self._w(t, "  " + str(port) + "/tcp ", "l")
                self._w(t, info["svc"] + " - ", "s")
                self._w(t, info["desc"] + "\n", "v")
                if info.get("banner"):
                    b = info["banner"].replace("\n", " ")[:120]
                    self._w(t, "    Banner: ", "l"); self._w(t, b + "\n", "b")
        else:
            self._w(t, "  No open ports.\n", "l")

        # ═══ THREAT ═══
        t = self.texts["THREAT"]
        self._clr(t)
        th = R.get("threat", {})
        sc = th.get("score", 0); lv = th.get("level", "UNKNOWN"); lt = lv.lower()
        self._w(t, "\n  +" + H + "+\n", "ts")
        self._w(t, "  |  THREAT INTELLIGENCE                          |\n", "ts")
        self._w(t, "  +" + H + "+\n\n", "ts")
        self._w(t, "  SCORE: ", "l")
        self._w(t, str(sc) + "/100 ", lt + "s")
        self._w(t, "[" + lv + "]\n\n", lt + "s")
        self._w(t, "  INDICATORS:\n", "ts")
        for reason in th.get("reasons", []):
            tag = "d" if "blacklist" in reason.lower() or "tor" in reason.lower() else "s"
            self._w(t, "  > " + reason + "\n", tag)
        bl = R.get("blacklist", [])
        if bl:
            self._w(t, "\n  BLACKLISTED ON " + str(len(bl)) + ":\n", "d")
            for b in bl:
                self._w(t, "  [X] " + b + "\n", "d")
        else:
            self._w(t, "\n  [OK] Clean on all blacklists\n", "s")
        self._w(t, "\n  TOR: ", "l")
        self._w(t, ("YES" if R.get("tor") else "NO") + "\n", "d" if R.get("tor") else "s")
        if cl:
            self._w(t, "  CLOUD: ", "l"); self._w(t, cl + "\n", "w")
        geo = R.get("geo") or {}
        if geo.get("proxy"):
            self._w(t, "  PROXY/VPN: ", "l"); self._w(t, "DETECTED\n", "d")

        # ═══ IoT/CCTV ═══
        t = self.texts["IOT/CCTV"]
        self._clr(t)
        iot = R.get("iot", [])
        if iot:
            self._w(t, "\n  IOT / CCTV / ICS DEVICES DETECTED\n\n", "ts")
            for dev in iot:
                risk = dev.get("risk", "LOW")
                rtag = "d" if risk == "CRITICAL" else "w" if risk == "HIGH" else "c" if risk == "MEDIUM" else "s"
                self._w(t, "  [" + risk + "] ", rtag)
                self._w(t, dev.get("device_type", "") + " on port ", "v")
                self._w(t, str(dev.get("port", "")) + " (" + dev.get("service", "") + ")\n", "i")
        else:
            self._w(t, "\n  No IoT/CCTV signatures detected.\n", "l")
            self._w(t, "  Run DEEP SCAN for extended port coverage.\n", "i")

        # ═══ WHOIS ═══
        t = self.texts["WHOIS"]
        self._clr(t)
        wd = R.get("whois")
        if wd:
            self._w(t, "\n  WHOIS RECORD\n\n", "ts")
            for line in wd.splitlines():
                if ":" in line and len(line.split(":")) == 2:
                    k, v = line.split(":", 1)
                    self._w(t, "  " + k.strip() + ": ", "i"); self._w(t, v.strip() + "\n", "v")
                elif line.strip():
                    self._w(t, "  " + line + "\n")
        else:
            self._w(t, "\n  WHOIS unavailable or deep scan required.\n", "l")

        # ═══ TRACE ═══
        t = self.texts["TRACE"]
        self._clr(t)
        td = R.get("trace")
        if td:
            self._w(t, "\n  TRACEROUTE\n\n", "ts")
            for line in td:
                self._w(t, "  " + line + "\n", "v")
        else:
            self._w(t, "\n  Traceroute unavailable or deep scan required.\n", "l")

        # ═══ DASHBOARD ═══
        t = self.texts["DASHBOARD"]
        self._clr(t)
        self._w(t, "\n  INTELLIGENCE DASHBOARD\n\n", "ts")
        stats = self.db.get_scan_stats()
        sessions = self.db.get_sessions()
        self._w(t, "  Total Scans:   ", "l"); self._w(t, str(stats["total"]) + "\n", "v")
        self._w(t, "  Threats Found: ", "l"); self._w(t, str(stats["threats"]) + "\n", "d")
        self._w(t, "  Active Sessions: ", "l"); self._w(t, str(len(sessions)) + "\n\n", "v")

        # Anomaly detection
        anomaly = Engine.anomaly_detect(self.scan_history)
        self._w(t, "  +- AI ANOMALY DETECTION " + "-" * 24 + "+\n", "ts")
        self._w(t, "  Mean Threat: ", "l"); self._w(t, str(anomaly.get("mean", 0)) + "\n", "v")
        self._w(t, "  Std Dev:     ", "l"); self._w(t, str(anomaly.get("std", 0)) + "\n", "v")
        if anomaly.get("anomalies"):
            self._w(t, "  ANOMALIES:\n", "d")
            for a in anomaly["anomalies"]:
                self._w(t, "    " + a["ip"] + " score:" + str(a["score"]) + " dev:" + str(a["deviation"]) + "x\n", "w")
        else:
            self._w(t, "  No anomalies detected.\n", "s")

        # Session tracking
        if sessions:
            self._w(t, "\n  +- SESSION TRACKING " + "-" * 28 + "+\n", "ts")
            for s in sessions[:15]:
                self._w(t, "  " + str(s[2]) + " | ", "l")
                self._w(t, s[1] + " | ", "v")
                self._w(t, "visits:" + str(s[4]) + " | last:" + str(s[3])[:19] + "\n", "i")

        # Shodan data
        shodan = R.get("shodan")
        if shodan:
            self._w(t, "\n  +- SHODAN INTERNETDB " + "-" * 27 + "+\n", "ts")
            for k, v in shodan.items():
                self._w(t, "  " + str(k) + ": ", "l")
                self._w(t, str(v) + "\n", "v")

        # ═══ RAW ═══
        t = self.texts["RAW"]
        self._clr(t)
        disp = dict(R)
        for k in ["whois", "interfaces", "arp", "alive_hosts", "routes"]:
            if disp.get(k) and isinstance(disp.get(k), (list, str)) and len(str(disp.get(k))) > 500:
                disp[k] = str(disp[k])[:300] + "..."
        self._w(t, json.dumps(disp, indent=2, default=str))

        # ═══ SIDE PANEL ═══
        self._update_side(R)

    def _update_side(self, R):
        ip = R["ip"]
        geo = R.get("geo") or {}
        th = R.get("threat", {})

        self.qi["IP"].config(text=ip)
        self.qi["Type"].config(text="PRIVATE" if R.get("private") else "PUBLIC",
                                fg=C.GLOW_G if R.get("private") else C.GLOW_O)
        self.qi["Country"].config(text=str(geo.get("country", "N/A")))
        self.qi["City"].config(text=str(geo.get("city", "N/A")))
        self.qi["ISP"].config(text=str(geo.get("isp", "N/A"))[:18])
        cl = R.get("cloud")
        self.qi["Cloud"].config(text=cl or "None", fg=C.GLOW_C if cl else C.TXT3)
        self.qi["Proxy"].config(text="YES" if geo.get("proxy") else "No",
                                 fg=C.GLOW_R if geo.get("proxy") else C.TXT3)
        self.qi["Tor"].config(text="YES" if R.get("tor") else "No",
                               fg=C.GLOW_R if R.get("tor") else C.TXT3)
        opc = len(R.get("open_ports", {}))
        self.qi["Ports"].config(text=str(opc) + " open", fg=C.GLOW_O if opc > 0 else C.TXT3)

        os_fp = R.get("os_fp", {})
        self.qi["OS"].config(text=os_fp.get("os", "?")[:15], fg=C.GLOW_C)

        iot = R.get("iot", [])
        self.qi["IoT"].config(text=str(len(iot)) + " found" if iot else "None",
                               fg=C.GLOW_R if iot else C.TXT3)

        sc = th.get("score", 0)
        lv = th.get("level", "N/A")
        cm = {"LOW": C.GLOW_G, "MODERATE": C.GLOW_Y, "HIGH": C.GLOW_O, "CRITICAL": C.GLOW_R}
        col = cm.get(lv, C.TXT3)
        self.thr_score.config(text=str(sc), fg=col)
        self.thr_level.config(text=lv, fg=col)
        self.thr_cv.delete("all")
        bw = (sc / 100) * 220
        self.thr_cv.create_rectangle(0, 0, bw, 18, fill=col, outline="")
        self.thr_cv.create_rectangle(bw, 0, 220, 18, fill=C.ABYSS, outline="")

    def _hist_sel(self, event):
        sel = self.hist.curselection()
        if sel:
            item = self.hist.get(sel[0])
            parts = item.split("] ")
            if len(parts) >= 2:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, parts[1].strip())

    def _clear(self):
        for w in self.texts.values():
            self._clr(w)
        self.entry.delete(0, tk.END)
        self.thr_score.config(text="--", fg=C.TXT3)
        self.thr_level.config(text="NO DATA", fg=C.TXT3)
        self.thr_cv.delete("all")
        for k in self.qi:
            self.qi[k].config(text="--", fg=C.TXT)
        self._stat("READY", C.GLOW_G)
        self._prog("")


# ════════════════════════════════════════════════════════════════
# SPLASH
# ════════════════════════════════════════════════════════════════

def splash():
    sp = tk.Tk()
    sp.overrideredirect(True)
    sp.configure(bg=C.VOID)
    w, h = 700, 420
    sp.geometry(str(w) + "x" + str(h) + "+" + str((sp.winfo_screenwidth()-w)//2) + "+" + str((sp.winfo_screenheight()-h)//2))
    cv = tk.Canvas(sp, width=w, height=h, bg=C.VOID, highlightthickness=0)
    cv.pack()

    for i in range(25):
        y = 40 + i * 15
        cv.create_line(30, y, 670, y, fill="#080818", width=1)

    cv.create_text(w//2, 60, text="VIPER-EYE", fill=C.GLOW_G, font=("Consolas", 36, "bold"))
    cv.create_text(w//2, 105, text="Ultimate IP Intelligence & Tracking Suite", fill=C.TXT2, font=("Consolas", 13))
    cv.create_text(w//2, 130, text="v3.0.0  //  ULTIMATE EDITION", fill=C.TXT3, font=("Consolas", 10))
    cv.create_text(w//2, 165, text="_" * 50, fill=C.DIM, font=("Consolas", 8))

    feats = [
        "GEOLOCATION + ISP/ASN FINGERPRINTING", "VPN/PROXY/TOR DETECTION",
        "IOT/CCTV DEVICE DISCOVERY", "OS FINGERPRINTING (TTL ANALYSIS)",
        "MAC VENDOR LOOKUP", "SHODAN INTERNETDB INTEGRATION",
        "DARK WEB EXPOSURE CHECK (HIBP)", "TRACKING LINK GENERATOR",
        "DISCORD WEBHOOK ALERTS", "AI ANOMALY DETECTION",
        "SESSION TRACKING + REVISIT DETECTION", "EXIF METADATA EXTRACTION",
        "EMAIL HEADER IP EXTRACTION", "WIFI NETWORK SCANNING",
        "EXPORT JSON/CSV REPORTS", "REAL-TIME THREAT GRAPH",
        "SQLITE DATABASE + ENCRYPTED STORAGE", "MULTI-TOOL PANEL",
    ]
    for i, f in enumerate(feats):
        x = w//4 if i < 9 else 3*w//4
        y = 195 + (i % 9) * 18
        cv.create_text(x, y, text=f, fill=C.GLOW_C, font=("Consolas", 8, "bold"))

    cv.create_text(w//2, 390, text="INITIALIZING...", fill=C.GLOW_R, font=("Consolas", 10))
    sp.update()
    for _ in range(14):
        sp.update()
        time.sleep(0.12)
    sp.destroy()


# ════════════════════════════════════════════════════════════════
# ENTRY
# ════════════════════════════════════════════════════════════════

def main():
    splash()
    root = tk.Tk()
    app = ViperEye(root)
    root.bind("<Control-l>", lambda e: app.entry.focus_set())
    root.bind("<Control-s>", lambda e: app._scan())
    root.bind("<Control-d>", lambda e: app._deep())
    root.bind("<Escape>", lambda e: app._clear())
    root.mainloop()

if __name__ == "__main__":
    main()