"""payments-api: a tiny HTTP service that talks to its database."""

import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

import db


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path != "/db":
            self._send(200, {"service": "payments-api", "ok": True})
            return
        url = os.environ.get("DATABASE_URL")
        if not url:
            self._send(503, {"ok": False, "error": "DATABASE_URL is not set"})
            return
        try:
            db.connect().command("ping")
            self._send(200, {"ok": True})
        except Exception as exc:  # noqa: BLE001 - a demo, report whatever failed
            self._send(503, {"ok": False, "error": str(exc)})

    def _send(self, status, body):
        self.send_response(status)
        self.send_header("content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(body).encode())

    def log_message(self, *args):
        pass


HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
