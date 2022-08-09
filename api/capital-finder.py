from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    params = parse.urlsplit(self.path)
    params_list = parse.parse_qsl(params.query)
    msg = str(params_list)      

  
    self.wfile.write(msg.encode())
    print(msg)
    print(msg.encode())
    return
