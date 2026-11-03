#!/usr/bin/env python3
"""
Canary Trap / Decoy Service
Logs incoming unauthorized connection probes and inspection attempts.
"""

from datetime import datetime
from flask import Flask, make_response, request

app = Flask(__name__)

# Log file for recording probes
LOG_FILE = "probe_activity.log"


def log_interaction(req):
    timestamp = datetime.utcnow().isoformat()
    client_ip = req.remote_addr
    user_agent = req.headers.get("User-Agent", "Unknown")
    method = req.method
    path = req.path

    log_entry = (
        f"[{timestamp}] PROBE DETECTED | IP: {client_ip} | Method: {method} | "
        f"Path: {path} | User-Agent: {user_agent}\n"
    )

    print(log_entry.strip())
    with open(LOG_FILE, "a") as f:
        f.write(log_entry)


@app.route("/", defaults={"path": ""}, methods=["GET", "POST", "PUT", "DELETE"])
@app.route("/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def catch_all(path):
    log_interaction(request)

    # Return a convincing default response to keep automated scanners talking
    response = make_response("<html><body><h1>Site Under Maintenance</h1></body></html>", 200)
    response.headers["Server"] = "Apache/2.4.41 (Ubuntu)"
    return response


if __name__ == "__main__":
    # Run on a local decoy port (e.g., port 8080 or 80)
    print("[*] Starting Canary Trap on port 8080...")
    app.run(host="0.0.0.0", port=8080)
