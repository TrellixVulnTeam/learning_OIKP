import geocoder
import requests
from urllib.parse import quote_plus
from pymongo import MongoClient
from bs4 import BeautifulSoup
from haversine import haversine
import pandas as pd
from collections import defaultdict
from tabulate import tabulate
import folium
import numpy as np



class Gwanggaeto:
    db = MongoClient('localhost',27017).encore1
    collection = db.pro3

    #to match category from search with target location
    search_category_result = []

    #when choosing location
    boundary = ""

    #store list based on search word
    store_list = ""

    #user's interest
    user_interest_category= ""

    #final choice of user
    final_choice = ""



    def __init__(self,search):
        self.collection.drop_index([("Coordinate","2dsphere")])
        self.collection.create_index([("Coordinate","2dsphere")],unique=True)
        self.search = search
        self.user_interest = ""


        #퍼센트변환
        escape = quote_plus(self.search)

        #header
        headers = {'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")}
        url = f"https://m.map.naver.com/search2/searchMore.naver?query={escape}&sm=clk&style=v5&page=1&displayCount=75&type=SITE_1"
        url_r =requests.get(url,headers=headers)


        #boundary
        boundary = url_r.json()['result']['boundary']
        self.boundary = [[float(boundary[0]),float(boundary[1])],[float(boundary[2]),float(boundary[3])]]

        #list of category based on search word.
        self.store_lst = url_r.json()['result']['site']['list']
        self.search_category_result = list(set([i['category'][-1] for i in self.store_lst]))

        #print(self.search_category_result)

        #Query based on exitsting DB  -> putting list of categories from the search result, boundary for the region.

        cursor = self.existing_DB() #without interest part

        if cursor.alive:
            print(f"The search result for '{self.search}', its categories, and its Average-star-rate(ASR) are as follows.\n")

            dic = defaultdict(list)

            #beautifying table, yet not working
            for i in cursor:
                dic['Category'].append("_".join(i['_id']))
                dic['ASR'].append(i['Avg_rate'])
                dic['# of stores'].append(i['점포수'])

            df = pd.DataFrame(dic)
            df.index +=1 #인덱스 1번부터 시작
            print(tabulate(df,headers="keys",tablefmt="psql"))
            print()
            scrap_ = input("현재 검색어와 데이터베이스 정보를 대조하여 얻은 결과입니다. 더 많은 정보를 원하시면 1번을 눌러주세요! \n: ")
            if scrap_ =='1':
                self.scrapping()
                self.__init__(self.search)
            else:

                #get user's interest
                choice = input("\nPress the number of category you are interested in! \n: ")
                self.user_interest = df._get_value(int(choice), 'Category').split('_')
                print(f"\n'{df._get_value(int(choice),'Category')}'is chosen. The details of the business will be printed out below.")

                cursor2 = self.existing_DB(self.user_interest) #with interest part

                dic2 = defaultdict(list)
                for i in cursor2:
                    dic2['Brand'].append(i['Brand'])
                    dic2['Rate'].append(i['Rate'])
                    dic2['Address'].append(i['Address'])
                    dic2['Tel'].append(i['Tel'])
                    dic2['OPhours'].append(i['OPhours'])
                    dic2['Coordinate'].append(i['Coordinate'])
                    dic2['Category'].append(i['Category'])
                self.user_interest = dic2

                df2 = pd.DataFrame(dic2)
                df2.index +=1
                print(tabulate(df2,headers="keys",tablefmt="psql"))
                choice2 =input("\nChoose an index you are interested in! \n: ")
                self.final_choice = (df2._get_value(int(choice2),'Brand'),
                                     df2._get_value(int(choice2),'Coordinate'),
                                     df2._get_value(int(choice2),'Address'),
                                     df2._get_value(int(choice2),'Tel'),
                                     df2._get_value(int(choice2),'OPhours'),
                                     df2._get_value(int(choice2),'Rate'),
                                     df2._get_value(int(choice2),'Category'))
                self.geo()

        else:
            print("Database Not Found: Call a function -- self.scrapping()\n")
            a = input("Wanna call the function? Press 1 \n: ")
            if a =='1':
                self.scrapping()
                self.__init__(self.search)



    def existing_DB(self,interest =None):
        if interest ==None:
            cursor = self.collection.aggregate([{"$match": {"Coordinate": {"$geoWithin": {"$box": self.boundary}},"Category" :{"$in":self.search_category_result}}},
                                           {"$group":
                                                {"_id": "$Category", "Avg_rate": {"$avg": "$Rate"}, "점포수": {"$sum": 1}}},
                                           {"$sort": {"Avg_rate": -1, "점포수": -1}},
                                           {"$project": {"_id": 1, "Avg_rate": {"$round": ["$Avg_rate", 2]}, "점포수": 1}},
                                           {"$limit": 5} ])
            return cursor
        else:
            cursor = self.collection.aggregate([{"$match": {"Coordinate": {"$geoWithin": {"$box": self.boundary}},"Category":interest}},
                                                {"$sort": {"Rate": -1}},
                                                {"$project": {"_id": 0, "Brand":1,"Rate": 1, "Tel":1,"OPhours":1,"Address":1,"Coordinate":1,"Category":1}}
                                                   #,{"$limit": 5}
                                                ])
            return cursor

    def scrapping(self):
        store_lst = self.store_lst

        for i in store_lst:
            name = i['name']
            category = i['category']
            addr = i['address']
            coord = [float(i['x']), float(i['y'])]
            tel = i['telDisplay']
            unique = i['id']
            key_for_second_page=unique[1:]
            soup = self.parse_html(key_for_second_page)
            try:
                operating_hours = soup.find('div',class_="_2ZP3j").get_text()
                star_rate  = float(soup.find("span",class_="_1Y6hi _1A8_M").em.string)
                self.collection.insert_one({"_id":unique,"Brand":name,"Category":category,"Rate":star_rate,"Address":addr,"Coordinate":coord,"OPhours": operating_hours,"Tel":tel})
            except:
                continue
        else:
            self.existing_DB(self.user_interest)


    #to get star-rate
    def parse_html(self,get_id):
        list_url = f'https://m.place.naver.com/restaurant/{get_id}/home'
        response = requests.get(list_url)
        response.encoding = 'UTF-8'
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    def geo(self):
        #m = folium.Map([self.final_choice[1][1],self.final_choice[1][0]], zoom_start=15)
        center_point= np.array(self.user_interest["Coordinate"]).mean(axis=0)
        m= folium.Map([center_point[1],center_point[0]],zoom_start=15)
        for i in range(len(self.user_interest["Coordinate"])):
            #distance = round(haversine((geocoder.ip('me').latlng[1],geocoder.ip('me').latlng[0]), self.user_interest['Coordinate'][i]),2)
            distance = round(haversine((126.779519,37.4884377), self.user_interest['Coordinate'][i]),2)
            html = f"""<h2>{self.user_interest['Brand'][i]}</h2><b>★{self.user_interest['Rate'][i]}</b><br>
                        <hr><br>
                        <b>주소 : {self.user_interest['Address'][i]}</b><br><br>
                        <b>운영시간 : {self.user_interest['OPhours'][i]}</b><br><br>
                        <b>전화번호 : {self.user_interest['Tel'][i]}</b><br><br>
                        <b>거리 : {distance}km away."""

            iframe = folium.IFrame(html)

            folium.Marker(location=[self.user_interest['Coordinate'][i][1],self.user_interest['Coordinate'][i][0]],
                          popup=folium.Popup(iframe,min_width=500,max_width=500),
                          icon=folium.Icon(color='orange'),
                          tooltip=self.user_interest['Brand'][i]).add_to(m)
        center_point= np.array(self.user_interest["Coordinate"]).mean(axis=0)
        folium.Marker(location=[center_point[1],center_point[0]],
                      popup=folium.Popup(self.weather_info(self.final_choice[2]),min_width=500,max_width=500),
                      icon=folium.Icon(color='green'),
                      tooltip="Weather Forecast").add_to(m)
        m.save('test.html')

    def weather_info(self, address):
        address = self.final_choice[2]
        result = ""
        url = 'https://dapi.kakao.com/v2/local/search/address.json?query=' + address
        rest_api_key = '2e05eca8e74f4d6b28c35a6ab2e4ae7c'
        header = {'Authorization': 'KakaoAK ' + rest_api_key}
        r = requests.get(url, headers=header)
        if r.status_code == 200:
            h_code = r.json()["documents"][0]["address"]['h_code']
            result = h_code
        else:
            result = "ERROR[" + str(r.status_code) + "]"

        url = f'https://www.kma.go.kr/wid/queryDFSRSS.jsp?zone={result}'
        xml = requests.get(url).text
        soup = BeautifulSoup(xml, 'html.parser')
        current_wf = soup.data
        time = current_wf.hour.string
        temp_now = current_wf.temp.string
        condition = current_wf.wfkor.string
        wind = current_wf.wdkor.string
        will_be_rainy = current_wf.pop.string
        humidity = current_wf.reh.string
        if condition in ['비','눈/비']:
            return f"""<h2><실시간 기상정보></h2><br><br><hr><h4><b>현재 해당 장소 날씨 정보 브리핑해드리겠습니다.<br>
            \r현재 {temp_now}정도의 온도로 날씨는 '{condition}'가 온다고 합니다. <br>
            \r바람은 {wind}쪽 방향으로 부는 가운데, 강수확률은 {will_be_rainy}% 입니다.<br>
            \r습도가 {humidity}%에 해당하니 적당히 잘 챙겨서 나가세요!</b></h4><br>\
            """
        elif condition == '눈':
            return f"""<h2><실시간 기상정보></h2><br><hr><h4><b>현재 해당 장소 날씨 정보 브리핑해드리겠습니다.<br>
                 \r현재 {temp_now}정도의 온도로 날씨는 '{condition}'이 온다고 합니다. <br>
                 \r바람은 {wind}쪽 방향으로 부는 가운데, 강수확률은 {will_be_rainy}% 입니다.<br>
                 \r습도가 {humidity}%에 해당하니 적당히 잘 챙겨서 나가세요!</b></h4><br>\
                """
        else:
            return f"""<h2><실시간 기상정보></h2><br><br><hr><h4><b>현재 해당 장소 날씨 정보 브리핑해드리겠습니다.<br>
                        \r현재 {temp_now}정도의 온도로 날씨는 '{condition}'입니다. <br>
                        \r바람은 {wind}쪽 방향으로 부는 가운데, 강수확률은 {will_be_rainy}% 입니다.<br>
                        \r습도가 {humidity}%에 해당하니 적당히 잘 챙겨서 나가세요!</b></h4><br>\
                        """


if __name__ == '__main__':
    a =Gwanggaeto("전주 고궁")
    print(a.final_choice)


