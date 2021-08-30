import requests

BASE = "http://127.0.0.1:5000/"

data = [{"likes":78, "name":"Joe","views":10000},
        {"likes":10000, "name":"How to make REST API","views":8000000},
        {"likes":35, "name":"tim","views":2000}
        ]
for i in range(len(data)):
    response = requests.put(BASE + "video/" +str(i), data[i] )
    print(response.json())

input()
response = requests.delete(BASE + "video/4")
print(response)

response = requests.get(BASE + "video/2")
print(response.json())
