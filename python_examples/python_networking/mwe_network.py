from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import time
import logging

# Logging so you can see what the connector is requesting
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
logger = logging.getLogger('FakeMISP')


class FakeMISP(BaseHTTPRequestHandler):

    # ---- Scenarios you can toggle ----
    SCENARIO = "no_answer_on_search"
    # Options:
    #   "no_answer_on_search"  → init works, search hangs forever
    #   "slow_answer"          → init works, search responds after delay
    #   "partial_response"     → init works, search sends headers then hangs
    #   "empty_events"         → init works, search returns 0 events
    #   "error_500"            → init works, search returns server error
    #   "no_answer_on_init"    → hangs on version check (never initializes)

    SLOW_DELAY = 60  # seconds for slow_answer scenario

    def do_GET(self, retry=False):
        path = self.path
        logger.info(f"GET {path}")

        # --- Step 1: Version check ---
        if 'getVersion' in path or 'getPyMISPVersion' in path:
            if self.SCENARIO == "no_answer_on_init":
                logger.info("Simulating no answer on init...")
                time.sleep(999999)
                return

            self._send_json({
                "version": "2.4.180",
                "perm_sync": False,
                "perm_sighting": False,
                "perm_galaxy_editor": False,
                "request_encoding": ["gzip"],
                "filter_sightings": False,
                "pymisp_recommended_version": "2.5.4"
            })
            return

        # --- Step 2: User validation ---
        if 'users/view/me' in path:
            self._send_json({
                "User": {
                    "id": "1",
                    "org_id": "1",
                    "role_id": "1",
                    "email": "admin@fake-misp.local",
                    "autoalert": False,
                    "invited_by": "0",
                    "change_pw": "0",
                    "termsaccepted": True,
                    "newsread": "0"
                },
                "Role": {
                    "id": "1",
                    "name": "admin",
                    "perm_add": True,
                    "perm_modify": True,
                    "perm_publish": True,
                    "perm_auth": True
                },
                "UserSetting": []
            })
            return

        # --- Catch-all for other GET requests ---
        self._send_json({"response": []})

    def do_POST(self):
        # Read the request body
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length) if content_length else b''

        path = self.path
        logger.info(f"POST {path}")
        logger.info(f"  Headers: Authorization={self.headers.get('Authorization', 'N/A')}")
        logger.info(f"  Body: {body.decode('utf-8', errors='replace')[:500]}")

        # --- Event search (where the connector fetches data) ---
        if 'events/restSearch' in path:

            if self.SCENARIO == "no_answer_on_search":
                logger.info("Simulating no answer on search (hanging)...")
                time.sleep(999999)
                return

            elif self.SCENARIO == "slow_answer":
                logger.info(f"Simulating slow answer ({self.SLOW_DELAY}s)...")
                time.sleep(self.SLOW_DELAY)
                self._send_json({"response": []})
                return

            elif self.SCENARIO == "partial_response":
                logger.info("Simulating partial response...")
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.send_header('Content-Length', '99999')  # promise data
                self.end_headers()
                self.wfile.write(b'{"response": [')  # start JSON
                self.wfile.flush()
                time.sleep(999999)  # never finish
                return

            elif self.SCENARIO == "empty_events":
                logger.info("Returning empty events")
                self._send_json({"response": []})
                return

            elif self.SCENARIO == "error_500":
                logger.info("Returning 500 error")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "name": "An Internal Error Has Occurred.",
                    "message": "An Internal Error Has Occurred.",
                    "url": "/events/restSearch"
                }).encode())
                return

        # --- Catch-all for other POST requests ---
        self._send_json({"response": []})

    def _send_json(self, data):
        """Helper to send a JSON response"""
        body = json.dumps(data).encode()
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format, *args):
        """Suppress default HTTP server logs (we use our own logger)"""
        pass


if __name__ == '__main__':
    PORT = 9999
    server = HTTPServer(('0.0.0.0', PORT), FakeMISP)
    logger.info(f"Fake MISP server running on port {PORT}")
    logger.info(f"Scenario: {FakeMISP.SCENARIO}")
    server.serve_forever()