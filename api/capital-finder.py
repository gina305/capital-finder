from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg = ""
    user_response =  ""
    url_components = parse.urlsplit(self.path)
    query_string_list = parse.parse_qsl(url_components.query)
    
  
    #Store user request values
    query_dict = dict(query_string_list)

    #Extract only the country
    for key, value in query_dict.items():
      if str(key.lower()) == "country":
        msg = str(value)
<<<<<<< HEAD
        url = 'https://restcountries.com/v3.1/name/' + msg

          #Create a http request

        break
    r = requests.get(url)
=======
        capital = getCapital(msg)
        break
     
>>>>>>> 72a00179d9b00cfd835a867f4688fc27da408d43

              #Saves the response as a dictionary
    r_objects = r.json() 

              #Extract and save the capital of the response
    capital = r_objects[0]
    capital = capital.get('capital')[0]
  
<<<<<<< HEAD
    user_response = f"The capital of {msg} is {capital}."

    if user_response == "":
      self.wfile.write("Please enter a valid request (i.e. /api/capital-finder?country=Bahamas)".encode())  
    
    else:
      self.wfile.write(user_response.encode()) 
=======
    user_response = f"The capital of {msg} is {capital}"

    

    #self.wfile.write(r_string.encode()) 

    def getCapital(country):
      url = 'https://restcountries.com/v3.1/name/Jamaica' + country

      #Create a http request
      r = requests.get(url)
>>>>>>> 72a00179d9b00cfd835a867f4688fc27da408d43

      #Saves the response as a dictionary
      r_objects = r.json() 

      #Extract and save the capital of the response
      capital = r_objects[0]
      capital = capital.get('capital')[0]
      return capital

    self.wfile.write(user_response.encode())  
    return