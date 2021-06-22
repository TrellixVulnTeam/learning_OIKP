import requests
import geocoder
from bs4 import BeautifulSoup as bs
import datetime

current = geocoder.ip('me').latlng
print(current)


#from KAKAO
def getLatLng(address):
    result = ""
    url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
    rest_api_key = '2e05eca8e74f4d6b28c35a6ab2e4ae7c'
    header = {'Authorization': 'KakaoAK ' + rest_api_key}
    r = requests.get(url, headers=header)
    if r.status_code == 200:
        h_code = r.json()["documents"][0]["address"]['h_code']
        result =  h_code
    else:
        result = "ERROR[" + str(r.status_code) + "]"

    return result


url = f'https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={getLatLng("부천시")}'
xml = requests.get(url).text
soup = bs(xml,'html.parser')
current_wf = soup.data
time = current_wf.hour.string
temp_now = current_wf.temp.string
condition = current_wf.wfkor.string
wind = current_wf.wdkor.string
will_be_rainy = current_wf.pop.string
humidity = current_wf.reh.string
print(f"""현재 해당 장소 날씨 정보 브리핑해드리겠습니다.
\r현재 {temp_now}정도의 온도로 날씨는 {condition}입니다.
\r바람은 {wind} 방향으로 부는 가운데, 강수확률은 {will_be_rainy}% 입니다.
\r습도가 {humidity}%에 해당하니 적당히 잘 챙겨서 나가세요!\
""")




