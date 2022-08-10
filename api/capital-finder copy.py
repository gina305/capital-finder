from http.server import BaseHTTPRequestHandler
from datetime import datetime
from urllib import parse
import requests
 
url = 'https://restcountries.com/v3.1/name/Jamaica'

#Create a http request
r = requests.get(url)

#Saves the response as a dictionary
r_objects = r.json() 

 #Extract and save the capital of the response
capital = r_objects[0]
capital = capital.get('capital')[0]

