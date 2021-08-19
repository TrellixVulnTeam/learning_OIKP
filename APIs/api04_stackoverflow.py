import requests
import json
from pprint import pprint
response = requests.get("https://api.stackexchange.com//2.3/questions?order=desc&sort=activity&site=stackoverflow")



for data in response.json()['items']:
    pprint(data)
