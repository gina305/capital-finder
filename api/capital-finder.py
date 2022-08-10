import enum
from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    msg=""
  
    query_dict = dict(query_string_list)


    for  item in query_dict:
      
      if query_dict["country"]:
        msg= str(item)
        break
    #msg="testing"


    #Call the country finder\

    self.wfile.write(msg.encode())
    return