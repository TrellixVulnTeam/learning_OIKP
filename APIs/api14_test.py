import requests
import json
data = [{"id":11,"password":12345,"name":"Jacy"},
        {"id":12,"password":12345,"name":"Cha"},
        {"id":13,"password":16225,"name":"Ke"},
        {"id":14,"password":82325,"name":"Kin"},
        {"id":15,"password":52225,"name":"Ohn"},
        ]

BASE = "http://127.0.0.1:5000/"

for i in data:
    response = requests.put(BASE+str(i['id']),i)
    print(response.json())

response = requests.post(BASE+"3", {"id":3,"password":16225,"name":"Key"})
print(response.json())



response = requests.get(BASE +"mongo/2",{"location":[126.97490812317584, 37.57851924892354]})
print(response.json())