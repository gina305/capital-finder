from http.server import BaseHTTPRequestHandler
from datetime import datetime

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg = self.path

    params = parse.urslplit(self.path)
    params_list = parse.parse_qsl(params.query)

    self.wfile.write(str(params_list))
    return
