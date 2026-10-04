
'''
backend.server
'''

from http.server import BaseHTTPRequestHandler, HTTPServer

import json


class Server(BaseHTTPRequestHandler):

    def do_GET(self):
        if self.path == "/message":
            data = {
                "message": "Hello from Python!"
            }

            response = json.dumps(data).encode()

            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()

            self.wfile.write(response)


server = HTTPServer(("localhost", 8000), Server)

print("Server running on http://localhost:8000")

server.serve_forever()
