import requests


BASE = "http://127.0.0.1:5000/"
data = [{"id":121,"name":"Jacky"},
        {"id":122,"name":"Karen"},
        {"id":123,"name":"Catalina"},
        {"id":124,"name":"Halapino"},
        {"id":125,"name":"Peach"}]

for i in data:
    response = requests.put(BASE+"registration/" + str(i['id']),i)

response = requests.get(BASE+"registration/121")
print(response.json())