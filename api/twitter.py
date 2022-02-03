

from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    # dic = dict(query_string_list)

 
    url = 'https://api.twitter.com/2/tweets/search/recent'
    r = requests.get(url)
    data = r.json()
    
    message = str(data)        
    # else:
    #     message = "Please give me a word to define"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return