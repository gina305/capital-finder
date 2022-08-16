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
            result = f"{city.upper()} is the capital of {query.upper()}."
            self.wfile.write(result.encode())
        else:

            self.wfile.write("Invalid entry. Try something like .../api/capital-finder/name=Bahamas".encode())
        return
