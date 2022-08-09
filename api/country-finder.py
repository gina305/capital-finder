from http.server import BaseHTTPRequestHandler
drom urllib import parse


class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    url_componenets = parse.urlsplit(self.path)

    msg ="is it working again?"
    self.wfile.write(msg.encode())
    return 