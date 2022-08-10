from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg = ""
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    
  
    #Store user request values
    query_dict = dict(query_string_list)
    

    #Extract only the country
    for key, value in query_dict.items():
      if str(key.lower()) == "country":
        msg = str(value)

    if msg == "":
      self.wfile.write("Invalid query. Enter a country. I.e. /api/capital-finder?country=Bahamas".encode())
    else:
      self.wfile.write(msg.encode())

    self.wfile.write(msg.encode())
    return