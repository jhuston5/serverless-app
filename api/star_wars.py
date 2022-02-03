from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)

    if "term" in dic:
      url = 'https://swapi.dev/api/'
      r = requests.get(url + dic['term'])
      data = r.json()
      sw_collection = []
      for sw in data:
            definition = sw
            sw_collection.append(definition)
    


      message = str(sw_collection)        
    else:
        message = "Please give me people, planets, films, species, vehicles, or starships to render"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return