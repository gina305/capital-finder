from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    # url_components = parse.urlsplit(self.path)
    # query_string_list = parse.parse_qsl(url_components.query)
    
  

    #query_dict = dict(query_string_list)
    #msg = str(query_dict)
    msg="testing"

    self.wfile.write(msg.encode())
    return