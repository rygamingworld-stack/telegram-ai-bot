from http.server import BaseHTTPRequestHandler
import json


class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()

        response = {
            "status": "online",
            "message": "Telegram AI Bot is running!"
        }

        self.wfile.write(json.dumps(response).encode("utf-8"))