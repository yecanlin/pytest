from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from os import path

data = {'result': 'this is a test'}

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class myServer(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            with open(path.realpath("./web/index.html"), 'rb') as f:
                content = f.read()
                print(self.path)
                self.send_response(200,"test")
                self.send_header('Content-type','text/html')
                self.end_headers()
                # Send the html message
                # self.wfile.write(json.dumps(data).encode())
                self.wfile.write(content)
        except  IOError:
            self.send_error(404,'File Not Found')
run(handler_class=myServer)