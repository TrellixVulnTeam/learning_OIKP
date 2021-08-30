# import geocoder
# g = geocoder.ip('me').latlng
# print([g[1],g[0]])

import reques
import urllib.parse

address = '부천시 심곡동'
url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) +'?format=json'

response = reques.get(url).json()
print(response)
print(response[0]["lat"])
print(response[0]["lon"])

import socket
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)
print("Your Computer Name is:" + hostname)
print("Your Computer IP Address is:" + IPAddr)



