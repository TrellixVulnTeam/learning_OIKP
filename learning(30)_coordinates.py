import googlemaps


gmaps = googlemaps.Client(key='AIzaSyCa-rXujn1Y_t5H_QlArcuBdhulWl-Ll64') #

# Geocoding an address
geocode_result1 = gmaps.geocode('경기도 부천시 지봉로 43-3')


lat1 = geocode_result1[0]['geometry']['location']['lat']
lng1 = geocode_result1[0]['geometry']['location']['lng']



print(lat1,lng1)
