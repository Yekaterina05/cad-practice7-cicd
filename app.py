import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer


def response_for(path):
    if path == "/health":
        return 200, {"status": "ok"}
    if path == "/":
        return 200, {
            "message": "Practice 7: CI/CD on AWS",
            "student": "Yekaterina Pyurko",
            "version": os.getenv("APP_VERSION", "local"),
        }
    return 404, {"error": "Not found"}


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        status, payload = response_for(self.path)
        body = json.dumps(payload).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), Handler).serve_forever()
