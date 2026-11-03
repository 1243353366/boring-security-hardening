#!/usr/bin/env python3
"""DEFENSIVE HONEYPOT - authorized lab / owned network only.

Listens on 127.0.0.1:2222, accepts connections, records source, banner,
and commands, then disconnects. It does NOT provide a real shell.

Run: python3 defensive_honeypot.py
Connect: nc 127.0.0.1 2222
"""
import socket, threading, datetime, json, os

HOST, PORT = "127.0.0.1", 2222
LOG = "honeypot_events.jsonl"

def log(event):
    event["timestamp"] = datetime.datetime.utcnow().isoformat() + "Z"
    with open(LOG, "a") as f:
        f.write(json.dumps(event) + "\n")
    print(json.dumps(event))

def handle(conn, addr):
    ip, port = addr
    log({"event": "connection", "src_ip": ip, "src_port": port})
    try:
        conn.settimeout(10)
        conn.sendall(b"SSH-2.0-OpenSSH_8.9p1\r\n")
        while True:
            data = conn.recv(4096)
            if not data:
                break
            log({"event": "input", "src_ip": ip, "data": data.decode(errors="replace")[:2000]})
    except Exception as e:
        log({"event": "error", "src_ip": ip, "error": str(e)})
    finally:
        conn.close()

def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
        srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        srv.bind((HOST, PORT))
        srv.listen(50)
        print(f"Honeypot listening on {HOST}:{PORT}; logging to {LOG}")
        while True:
            conn, addr = srv.accept()
            threading.Thread(target=handle, args=(conn, addr), daemon=True).start()

if __name__ == "__main__":
    main()
