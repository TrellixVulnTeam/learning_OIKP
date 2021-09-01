import requests
import json
data = [{"id":1,"password":1234225,"name":"Jacky"},
        {"id":2,"password":12345,"name":"Chan"},
        {"id":3,"password":16225,"name":"Key"},
        {"id":4,"password":8234225,"name":"Kian"},
        {"id":5,"password":5234225,"name":"Kon"},
        ]

BASE = "http://127.0.0.1:5000/"

for i in data:
    response = requests.put(BASE+str(i['id']),i)
    print(response.json())

response = requests.post(BASE+"3", {"id":3,"password":16225,"name":"Key"})
print(response.json())



response = requests.get(BASE +"mongo/2",{"location":[126.97490812317584, 37.57851924892354]})
print(response.json())