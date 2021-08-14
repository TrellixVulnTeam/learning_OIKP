from haversine import haversine, Unit

lyon = (45.7597, 4.8422) # (lat, lon)
Seoul = (37.565577,126.978082)
paris = (48.8567, 2.3508)
Busan = (35.1379222,129.05562775)
print(haversine(Seoul,Busan)) #in kilometers

print(tuple(Unit))


