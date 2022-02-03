import tweepy
import configparser

# Read configs
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret = config['twitter']['access_token_secret']

print(api_key)
print(api_key_secret)

print(access_token)
print(access_token_secret)

# authentication
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# public_tweets = api.home_timeline()
cursor = tweepy.Cursor(api.user_timeline, id='realDonaldTrump').items(1)
print(cursor)
for i in cursor:
  print(i)
# print(public_tweets)

# from http.server import BaseHTTPRequestHandler
# from urllib import parse
# import requests

# class handler(BaseHTTPRequestHandler):

#   def do_GET(self):
#     url_path = self.path
#     url_components = parse.urlsplit(url_path)
#     query_string_list = parse.parse_qsl(url_components.query)
#     # dic = dict(query_string_list)

 
#     url = 'https://api.twitter.com/2/tweets/search/recent'
#     r = requests.get(url)
#     data = r.json()
    
#     message = str(data)        
#     # else:
#     #     message = "Please give me a word to define"

#     self.send_response(200)
#     self.send_header('Content-type', 'text/plain')
#     self.end_headers()

#     self.wfile.write(message.encode())

#     return

  # API key
# k1XdZLB5rsKJS8moS9LstEtC7

  # API Key Secret
  # 28EcEbk643OV6k0yIYUSPFA7xuDILoQOiBlK7KhoZYbDDpaYkk

  # Bearer Token
  # AAAAAAAAAAAAAAAAAAAAACQ%2BYwEAAAAAYXPOt8yjlaz1n1F54%2BDwTMMPIhY%3DxGccmhsY2mLac2tBF61oLG1yeW83oCgGysQFLG12i7bjV0JckK

  # Access Token
  # 1333112564490719232-SugT3NDCXnuS9YyOQyrqOBTt2DiBaC

  # Access Token Secret
  # VxknV6Am3O3q2s6ManiHgylQvfAOUeP0Um7DtDlmVdBkm