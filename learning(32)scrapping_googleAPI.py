from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver.v2 as uc
import time
import googlemaps
import geocoder



def scrapping(loc,search):
    chrome_options = uc.ChromeOptions()
    chrome_options.add_argument('--headless') # 화면에 안뜨게 하는 것.
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    binary = 'C:\chromedriver_win32\chromedriver.exe'
    driver = uc.Chrome(binary,options=chrome_options)
    driver.get("https://m.map.naver.com/#/search")
    driver.maximize_window()


    # 검색창에 검색어 입력하기
    search_box = driver.find_element_by_xpath("/html/body/div[3]/div[1]/div[1]/form/div/div[2]/div/span[1]/input")
    search_box.send_keys(loc +" "+ search)
    search_box.send_keys(Keys.ENTER)


    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    list_ = soup.find_all('div',class_="item_info")

    for i in list_:
        item = "_".join(i.find("strong").text.split())
        category = i.find("em").text
        address = i.find('a', class_="item_address _btnAddress")
        unwanted = address.find('i')
        unwanted.extract()
        address = address.text.rstrip().split(maxsplit=2)
        print(item, category, address)
        coordinates = latlng(address)
    #상호명(pk), 카테고리, 주소, 좌표    +내 좌표  (내좌표랑 해당 추천된 곳과의 거리를 구하는거거든요)
    #CREATE TABLE () (상호명 : , 카테고리, 주소, 좌표 ,



    driver.close()

def latlng(address):
    gmaps = googlemaps.Client(key='your key') #
    # Geocoding an address
    geocode_result1 = gmaps.geocode(address)
    lat1 = geocode_result1[0]['geometry']['location']['lat']
    lng1 = geocode_result1[0]['geometry']['location']['lng']
    return [lat1,lng1]


def current_location():
    g = geocoder.ip('me').latlng
    return g