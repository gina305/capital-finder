from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests
import os

class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Necessary variables for parsing through string; also contains dicitonary
        params = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(params.query)
        query_dict = dict(query_string_list)

        if 'url' in query_dict:
              # set server settings
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # if the country exists, follow through code below
            source = query_dict['url']

            x= os.system(f"mammoth {source} output.html")
        
            
            self.wfile.write(x.encode())
        else:

            self.wfile.write("Invalid entry. Try something like .../api/capital-finder/name=Bahamas".encode())
        return
