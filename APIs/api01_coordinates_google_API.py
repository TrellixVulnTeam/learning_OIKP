import googlemaps
import geocoder
# Geocoding an address
import requests

def getLngLat_google():
    gmaps = googlemaps.Client(key='your_key') #
    #


    geocode_result1 = gmaps.geocode('경기도 부천시 지봉로 43-3')
    lat1 = geocode_result1[0]['geometry']['location']['lat']
    lng1 = geocode_result1[0]['geometry']['location']['lng']


    home = [geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]]
    destination = [lng1,lat1]
    return home,destination




import requests

#from KAKAO
def getLatLng(address):
    result = ""

    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '2e05eca8e74f4d6b28c35a6ab2e4ae7c'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)

    if r.status_code == 200:
        print(r.json())
        result_address = r.json()["documents"][0]["address"]

        result =  [result_address["x"], result_address["y"]]
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result




# main()
if __name__ == "__main__":

    #address = "서울 종로구 누상동 159-8"

    # 카카오 REST API로 좌표 구하기
    #address_latlng = getLatLng(address)
    #print(address_latlng)
    pass 
