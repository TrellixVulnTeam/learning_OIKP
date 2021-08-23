import requests

BASE = "http://127.0.0.1:5000/" #base url

response1 = requests.post(BASE+"helloworld")
print(response1.json())

response2 = requests.get(BASE+"helloworld")
print(response2.json())