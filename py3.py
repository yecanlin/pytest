from http.server import HTTPServer, BaseHTTPRequestHandler
import json

data = {'result': 'this is a test'}

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 8080)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

class myServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        self.send_response(200,"test")
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        # self.wfile.write(json.dumps(data).encode())
        self.wfile.write("<h1>hello world!</h1>".encode())
        return
run(handler_class=myServer)