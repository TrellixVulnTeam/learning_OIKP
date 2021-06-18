import geocoder
g = geocoder.ip('me').latlng
print([g[1],g[0]])