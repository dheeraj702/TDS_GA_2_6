import json
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Load student marks from q.json
        with open("q.json", "r") as f:
            marks_data = json.load(f)

        # Parse query parameters
        query = parse_qs(urlparse(self.path).query)
        names = query.get("name", [])

        # Get marks for each name
        marks = [marks_data.get(name, "Not Found") for name in names]

        # Prepare and send the response
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        response = json.dumps({"marks": marks})
        self.wfile.write(response.encode("utf-8"))
        return
