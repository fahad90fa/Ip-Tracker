"""Persistence helpers for scan history and sessions."""

import csv
import datetime
import io
import json
import sqlite3


class Database:
    def __init__(self, path: str = "viper_eye.db"):
        self.path = path
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.conn.execute("CREATE TABLE IF NOT EXISTS scans (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, ts TEXT, data TEXT, threat_score INTEGER, threat_level TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS sessions (id INTEGER PRIMARY KEY AUTOINCREMENT, ip TEXT, first_seen TEXT, last_seen TEXT, visit_count INTEGER DEFAULT 1)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS alerts (id INTEGER PRIMARY KEY AUTOINCREMENT, ts TEXT, type TEXT, message TEXT, severity TEXT)")
        self.conn.execute("CREATE TABLE IF NOT EXISTS links (id INTEGER PRIMARY KEY AUTOINCREMENT, uid TEXT, link TEXT, created TEXT, clicks INTEGER DEFAULT 0)")
        self.conn.commit()

    def save_scan(self, ip: str, data: dict, threat_score: int, threat_level: str) -> None:
        self.conn.execute("INSERT INTO scans (ip, ts, data, threat_score, threat_level) VALUES (?,?,?,?,?)",
                          (ip, datetime.datetime.now().isoformat(), json.dumps(data, default=str), threat_score, threat_level))
        self.conn.commit()

    def track_session(self, ip: str) -> None:
        row = self.conn.execute("SELECT * FROM sessions WHERE ip=?", (ip,)).fetchone()
        now = datetime.datetime.now().isoformat()
        if row:
            self.conn.execute("UPDATE sessions SET last_seen=?, visit_count=visit_count+1 WHERE ip=?", (now, ip))
        else:
            self.conn.execute("INSERT INTO sessions (ip, first_seen, last_seen) VALUES (?,?,?)", (ip, now, now))
        self.conn.commit()

    def get_sessions(self):
        return self.conn.execute("SELECT * FROM sessions ORDER BY last_seen DESC LIMIT 50").fetchall()

    def get_history(self, limit: int = 50):
        return self.conn.execute("SELECT * FROM scans ORDER BY id DESC LIMIT ?", (limit,)).fetchall()

    def add_alert(self, atype: str, message: str, severity: str) -> None:
        self.conn.execute("INSERT INTO alerts (ts, type, message, severity) VALUES (?,?,?,?)",
                          (datetime.datetime.now().isoformat(), atype, message, severity))
        self.conn.commit()

    def get_alerts(self):
        return self.conn.execute("SELECT * FROM alerts ORDER BY id DESC LIMIT 50").fetchall()

    def save_link(self, uid: str, link: str) -> None:
        self.conn.execute("INSERT INTO links (uid, link, created) VALUES (?,?,?)", (uid, link, datetime.datetime.now().isoformat()))
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
        for row in rows:
            writer.writerow([row[0], row[1], row[2], row[4], row[5]])
        return output.getvalue()
