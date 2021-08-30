from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import undetected_chromedriver.v2 as uc
import time
import geocoder
from functools import reduce
import reques
from pymongo import MongoClient
from haversine import haversine




class Gwanggaeto:
    client = MongoClient('localhost', 27017)
    db = client.encore1
    collection = db.pro3
    interest_point = [geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]]
    current_location = [geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]]
    interested_in = " "
    location_information = []


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

            #get coordinate

            coordinate= self.getLatLng(address)
            if coordinate != None:
                self.collection.insert_one({"brand":item,"category":category,"address":address,"location":coordinate})
                coordinates.append(coordinate)
                interest.append(category)
            else :
                continue
        #centerpoint
        driver.close()

        #set interest and location
        interest = tuple(set(interest))
        print(f"해당 지역 {self.loc}에서 {self.search}에 대한 하위 검색결과는 다음과 같습니다\n {'---'*30} ")
        print(", ".join(f"{i + 1}:" + interest[i] for i in range(len(interest))) +"\n")
        want = input(f"관심있는 곳의 번호를 입력해주시면 {self.loc} 중심에서 1km 이내의 장소들을 찾아드릴게요! \n: " )
        self.interested_in = interest[int(want)-1]

        # centerpoint
        x = reduce(lambda x, y: x + y, (i[0] for i in coordinates)) / len(coordinates)
        y = reduce(lambda x, y: x + y, (i[1] for i in coordinates)) / len(coordinates)
        center_point = [x,y]
        self.interest_point = center_point


    def getLatLng(self,address):
        result = ""

        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
        rest_api_key = '2e05eca8e74f4d6b28c35a6ab2e4ae7c'
        header = {'Authorization': 'KakaoAK ' + rest_api_key}
        r = reques.get(url, headers=header)

        if r.status_code == 200:
            try:
                result_address = r.json()["documents"][0]["address"]
                result = [float(result_address["x"]), float(result_address["y"])]
            except:
                return None
        else:
            result = "ERROR[" + str(r.status_code) + "]"

        return result



    def geo(self,geocenter,interest_in):
        try:
            self.collection.create_index([("location","2dsphere")])
        except Exception as E:
            pass
        finally:
            b = self.collection.aggregate([
                {"$geoNear": {
                "spherical": True,
                "maxDistance": 1000,
                "near":  {"type": "Point",
                         "coordinates": geocenter},
                "distanceField": "distance",
                "key": "location" }}
                ,{"$match": {"category" :interest_in}}
                ,{"$project":{"_id":0,"brand":1,"category":1,"distance":1,"address":1,"location":1}}
                #,{"$group":{"_id": "$brand","distance":{"$avg":"$distance"}}}
                ,{"$limit":10}
            ])
            for i in b:
                if (i['brand'], i['category'], i['address'], i['location']) not in self.location_information:
                    self.location_information.append((i['brand'], i['category'], i['address'], i['location']))
                else :
                    continue
         #set

            print(f"{self.loc} 주변의 {self.interested_in} 상위 {len(self.location_information)}개 검색결과 입니다.")
            print()
            for i in range(len(self.location_information)):
                print(str(i+1).ljust(3), self.location_information[i][0])
            print()
            choice = input("번호를 입력해 바로가기 : ")
            destination = self.location_information[int(choice)-1][3]
            distance_between = haversine(self.current_location, destination)
            print(f"목적지까지 {distance_between}km 만큼 떨어져 있습니다.\n해당 지역 날씨정보를 받으시겠습니까?")
            weather = input("1 : 예 \n2 : 아니오\n")
            if weather == '1':
                self.weather_info(self.location_information[int(choice) - 1][2])


    def weather_info(self,address):
        result = ""
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
        rest_api_key = '2e05eca8e74f4d6b28c35a6ab2e4ae7c'
        header = {'Authorization': 'KakaoAK ' + rest_api_key}
        r = reques.get(url, headers=header)
        if r.status_code == 200:
            h_code = r.json()["documents"][0]["address"]['h_code']
            result = h_code
        else:
            result = "ERROR[" + str(r.status_code) + "]"

        url = f'https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={result}'
        xml = reques.get(url).text
        soup = BeautifulSoup(xml, 'html.parser')
        current_wf = soup.data
        time = current_wf.hour.string
        temp_now = current_wf.temp.string
        condition = current_wf.wfkor.string
        wind = current_wf.wdkor.string
        will_be_rainy = current_wf.pop.string
        humidity = current_wf.reh.string
        print(f"""현재 해당 장소 날씨 정보 브리핑해드리겠습니다.
        \r현재 {temp_now}정도의 온도로 날씨는 {condition}입니다. 
        \r바람은 {wind}쪽 방향으로 부는 가운데, 강수확률은 {will_be_rainy}% 입니다.
        \r습도가 {humidity}%에 해당하니 적당히 잘 챙겨서 나가세요!\
        """)


    def distance_between(self):
        pass
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
    a1 = Gwanggaeto("개봉", "맛집")
    a1.scrapping()

    a1.geo(a1.interest_point,a1.interested_in)





