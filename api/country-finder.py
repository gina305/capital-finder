from http.server import BaseHTTPRequestHandler
drom urllib import parse


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()
    msg = self.path.encode()
    self.wfile.write(msg)
    return 