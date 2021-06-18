from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver.v2 as uc
import time
import googlemaps
import geocoder
from functools import reduce

from pymongo import MongoClient
import pprint
from bson.code import Code


class Gwanggaeto:
    client = MongoClient('localhost', 27017)
    db = client.encore1
    collection = db.pro3
    interest_point = [geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]]
    current_location = [geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]]
    interested_in = " "

    def __init__(self,loc,search):
        self.loc = loc
        self.search = search

    def scrapping(self): #setter + inserter
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
        search_box.send_keys(self.loc +" "+ self.search)
        search_box.send_keys(Keys.ENTER)

        time.sleep(3)

        html = driver.page_source
        soup = BeautifulSoup(html,'html.parser')
        list_ = soup.find_all('div',class_="item_info")


        #get info and insert them into MongoDB
        coordinates = []
        interest = []
        for i in list_:
            item = "_".join(i.find("strong").text.split())
            category = i.find("em").text
            address = i.find('a', class_="item_address _btnAddress")
            unwanted = address.find('i')
            unwanted.extract()
            address = address.text.strip()
            coordinate = self.latlng(address)
            address = address.split(maxsplit=2)
            self.collection.insert_one({"brand":item,"category":category,"address":address,"location":coordinate})
            coordinates.append(coordinate)
            interest.append(category)

        #centerpoint
        x = reduce(lambda x, y: x + y, (i[0] for i in coordinates)) / len(coordinates)
        y = reduce(lambda x, y: x + y, (i[1] for i in coordinates)) / len(coordinates)
        center_point = [x,y]

        driver.close()

        #set interest and location
        interest = tuple(set(interest))
        self.interest_point = center_point
        print(f"해당 지역 {self.loc}에서 {self.search}에 대한 하위카테고리는 다음과 같습니다: ")
        print(", ".join(f"{i + 1}:" + interest[i] for i in range(len(interest))))
        want = input("관심있는 곳의 번호를 입력해주시면 당신의 위치에서 가장 가까운 곳을 찾아드릴게요! :" )
        self.interested_in = interest[int(want)-1]



    def latlng(self, address):
        gmaps = googlemaps.Client(key='your key') #
        # Geocoding an address
        geocode_result1 = gmaps.geocode(address)
        lng1 = geocode_result1[0]['geometry']['location']['lng']
        lat1 = geocode_result1[0]['geometry']['location']['lat']
        return [lng1,lat1]


    def geo(self):
        geo_center = self.interest_point
        interest = self.interested_in
        try:
            self.collection.create_index({"location":"2dsphere"})
            a = self.collection.aggregate([{"$geoNear":{
                "spherical" : True,
                "maxDistance" : 500,
                "near":{"type": "Point",
                        "coordinates": self.interest_point},
                "distanceField":"distance",
                "key":"location"
            }}])
            for i in a:
                print(i)
        except Exception as E:
            b = self.collection.aggregate([
                {"$geoNear": {
                "spherical": True,
                "maxDistance": 10000000,
                "near":  {"type": "Point",
                         "coordinates": geo_center},
                "distanceField": "distance",
                "key": "location" }}
                ,{"$match": {"category" :interest}}
                ,{"$project":{"_id":0,"brand":1,"distance":1,"address":1,"location":1}}
                ,{"$group":{"_id": "$brand","distance":{"$avg":"$distance"}}}
                ,{"$limit":10}
            ])
            for i in b:
                print(i)





    # def pymong(self):
    #     # Connect
    #     client = MongoClient('localhost', 27017)
    #     db = client.test
    #
    #     # Insert new document
    #     db.pro3.insert_one({"33": 11, "69": 33})
    #     db.pro3.insert_many([{"33": 11, "69": 33}, {"53": 11, "69": 33}, {"43": 11, "69": 33}])
    #
    #     # AGGREGATE
    #     for i in db.places.aggregate([{"$project": {"manu_price": 1, "place": 1, "_id": 0}},
    #                                   {"$group": {"_id": "$place", "price": {"$avg": "$manu_price.Americano"}}}]):
    #         print(i)
    #
    #     # MAP REDUCE
    #     mr = Code("""function mymap(){
    #         if (this.manu_price.Americano != null){
    #         emit(this.place,{manu_price:this.manu_price.Americano})};
    #     }""")
    #
    #     red = Code("""function myred(key,values){
    #         var result = {price :0};
    #         var cnt = 0;
    #         values.forEach(function(v){
    #             result.price += v.manu_price;
    #             cnt +=1;
    #         })
    #         result.price /= cnt;
    #         return result;
    #     }""")
    #     db.places.map_reduce(mr, red, "res5")
    #     for i in db.res5.find():
    #         pprint.pprint(i)



if __name__ == '__main__':
    a1 = Gwanggaeto("신당동","떡볶이")
    center_point = a1.scrapping()
    a1.interested_in = ""
    a1.geo()


    #print(a1.interest_point)