#!/usr/bin/python3
import http.server
import json


class MyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == '/data':
            data = {
                "name": "John",
                "age": 30,
                "city": "New York"
            }
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")

def run_server(port=8000):
    server_address = ('', port)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print(f"Server running on port {port}...")
    print(f"Access it at: http://localhost:{port}")
    print("\nAvailable endpoints:")
    print(f"  - http://localhost:{port}/")
    print(f"  - http://localhost:{port}/data")
    print(f"  - http://localhost:{port}/status")

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\nServer stopped.")
        httpd.server_close()


if __name__ == "__main__":
    run_server()
    