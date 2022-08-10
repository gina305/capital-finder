from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import requests
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
      
      url = 'https://restcountries.com/v3.1/name/'
            query = msg
            query_url = url + query

            response = requests.get(query_url)
            data = response.json()

            parsed_country = data[0]['name']
            country = str(parsed_country['common'])
            result_str = f"{query.upper()} is the capital of {country.upper()}"

      self.wfile.write(result_str.encode())
      
      self.wfile.write(msg.encode())

    return