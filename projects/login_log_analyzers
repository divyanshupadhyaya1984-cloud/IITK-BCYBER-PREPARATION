#!/usr/bin/env python3
import os
import sys
import re
import time
import sqlite3
from datetime import datetime

# --- CONFIGURATION & PATHS ---
LOG_FILE = "/var/log/auth.log"
DB_FILE = os.path.expanduser("~/_Project/data/analyzer.db")
BRUTE_FORCE_THRESHOLD = 5  # Max failed attempts allowed in 60s
WINDOW_SECONDS = 60

# Regular Expression targeting modern Linux systemd/sshd failed logins
AUTH_FAIL_REGEX = r"(?P<ts>\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}).*sshd.*Failed password for (?P<invalid>invalid user )?(?P<user>\S+) from (?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})"

def init_db():
    """Establishes database schema with explicit indexes for analytical lookups."""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS login_events (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            epoch_time REAL,
            username TEXT,
            ip_address TEXT,
            status TEXT
        )
    """)
    # Essential index to optimize time-windowed SQL queries
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_time_ip ON login_events (epoch_time, ip_address);")
    conn.commit()
    conn.close()

def log_and_evaluate(username, ip):
    """Inserts failed event data and applies sliding-window detection logic."""
    current_epoch = time.time()
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    
    # 1. Ingestion: Save the freshly parsed event
    cursor.execute(
        "INSERT INTO login_events (epoch_time, username, ip_address, status) VALUES (?, ?, ?, 'FAILED')",
        (current_epoch, username, ip)
    )
    conn.commit()
    
    # 2. Dynamic Sliding Window Check
    # Formula: Count failures from this specific IP where (current_time - event_time) <= 60
    lookback_limit = current_epoch - WINDOW_SECONDS
    cursor.execute(
        "SELECT COUNT(*) FROM login_events WHERE ip_address = ? AND epoch_time > ? AND status = 'FAILED'",
        (ip, lookback_limit)
    )
    failure_count = cursor.fetchone()[0]
    conn.close()
    
    # 3. Decision Boundary Evaluation
    if failure_count >= BRUTE_FORCE_THRESHOLD:
        print(f"\n[⚠️ SECURITY ALERT] Brute-Force Footprint Detected!")
        print(f" -> Source IP: {ip}")
        print(f" -> Targeted User accounts: {username}")
        print(f" -> Event Metrics: {failure_count} malicious validation attempts within the last 60 seconds.\n" + "-"*60)

def tail_log():
    """Non-blocking log stream ingestion engine."""
    print(f"[*] Initializing Security Analyzer Ingestion Core against {LOG_FILE}...")
    try:
        # Move pointer directly to the end of the file to prevent reading historic logs
        file_size = os.path.getsize(LOG_FILE)
        with open(LOG_FILE, "r", errors="ignore") as f:
            f.seek(file_size)
            
            while True:
                line = f.readline()
                if not line:
                    time.sleep(0.1) # Cool down CPU loop
                    continue
                
                # Check line against our regex signature
                match = re.search(AUTH_FAIL_REGEX, line)
                if match:
                    gd = match.groupdict()
                    username = gd["user"]
                    ip_address = gd["ip"]
                    log_and_evaluate(username, ip_address)
                    
    except PermissionError:
        print("[!] Execution Failure: Root access required to read system auth logs. Run using 'sudo'.")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n[*] Gracefully shutting down security monitoring.")
        sys.exit(0)

if __name__ == "__main__":
    if not os.path.exists(os.path.dirname(DB_FILE)):
        os.makedirs(os.path.dirname(DB_FILE))
    init_db()
    tail_log()
