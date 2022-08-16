from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests


class handler(BaseHTTPRequestHandler):

    def do_GET(self):
        # Necessary variables for parsing through string; also contains dicitonary
        params = parse.urlsplit(self.path)
        query_string_list = parse.parse_qsl(params.query)
        query_dict = dict(query_string_list)

        if 'name' in query_dict:
              # set server settings
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            
            # if the country exists, follow through code below
            query = query_dict['name']

            #Request API data for this query
            query_url = 'https://restcountries.com/v3.1/name/' + query
            response = requests.get(query_url)
            data = response.json()

            #Extract query from returned data
            parsed_city = data[0]['capital']
            city = str(parsed_city[0])
            result = f"The capital of {query.upper()} is {city.upper()}"
            self.wfile.write(result.encode())
        else:

            self.wfile.write("Invalid entry. Try something like .../api/capital-finder/name=Bahamas".encode())
        return

# non-country is getting pushed into query_dict and therefore, gets passed into the "it statement". So it ends in a 502 and doesn't get to the else statement.