from http.server import BaseHTTPRequestHandler
drom urllib import parse


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg = f'{self.path}'
    self.wfile.write(msg.encode())
    return 