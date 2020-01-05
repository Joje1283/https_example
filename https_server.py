import http.server
import os
import ssl

if __name__ == '__main__':
    httpd = http.server.HTTPServer(('0.0.0.0', 5443), http.server.SimpleHTTPRequestHandler)
    certfile = os.path.realpath('private.crt')
    keyfile = os.path.realpath('private.key')
    httpd.socket = ssl.wrap_socket(httpd.socket, certfile=certfile, keyfile=keyfile)
    httpd.serve_forever()