from http import server
import http.server
import socketserver

def run(server_class=server.HTTPServer, handler_class=server.BaseHTTPRequestHandler):
    server_address = ('', 80)
    httpd = server_class(server_address, handler_class)
    print(httpd)
    httpd.serve_forever()


PORT = 80

Handler = http.server.SimpleHTTPRequestHandler
HandlerAnother = server.BaseHTTPRequestHandler

with socketserver.TCPServer(("", PORT), HandlerAnother) as httpd:
    print("serving at port: ", PORT)
    print(httpd.get_request)
    httpd.serve_forever()
    