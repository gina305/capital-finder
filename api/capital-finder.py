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
        url = 'https://restcountries.com/v3.1/name/' + msg

          #Create a http request

        break
    r = requests.get(url)

              #Saves the response as a dictionary
    r_objects = r.json() 

              #Extract and save the capital of the response
    capital = r_objects[0]
    capital = capital.get('capital')[0]
  
    user_response = f"The capital of {msg} is {capital}"

    self.wfile.write(user_response.encode())  

    #self.wfile.write(r_string.encode()) 



    return