from http.server import BaseHTTPRequestHandler
from urllib import parse
import requests

class handler(BaseHTTPRequestHandler):

  def do_GET(self):
    url_path = self.path
    url_components = parse.urlsplit(url_path)
    query_string_list = parse.parse_qsl(url_components.query)
    dic = dict(query_string_list)
    
    url = 'https://swapi.dev/api/'
    r = requests.get(url)
    data = r.json()
    
    sw_collection = []
    for sw in data:
          sw_val = sw
          sw_collection.append(sw_val)
    
    sw_search = requests.get(f"{url}/{sw_collection[0]}/1")
    message = str(sw_search)        

    # if "term" in dic:
    #   url = 'https://swapi.dev/api/'
    #   r = requests.get(url + dic['term'])
    #   data = r.json()
    # else:
    #     message = "Please give me people, planets, films, species, vehicles, or starships to render"

    self.send_response(200)
    self.send_header('Content-type', 'text/plain')
    self.end_headers()

    self.wfile.write(message.encode())

    return


    # {'people': 'https://swapi.dev/api/people/', 'planets': 'https://swapi.dev/api/planets/', 'films': 'https://swapi.dev/api/films/', 'species': 'https://swapi.dev/api/species/', 'vehicles': 'https://swapi.dev/api/vehicles/', 'starships': 'https://swapi.dev/api/starships/'}