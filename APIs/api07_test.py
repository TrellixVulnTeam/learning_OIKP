import requests

BASE = "http://127.0.0.1:5000/" #base url

#
response2 = requests.get(BASE+"helloworld/Migo")
print(response2.json())


response2 = requests.post(BASE+"helloworld/Craig")
print(response2.json())

