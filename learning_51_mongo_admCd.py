from pymongo import MongoClient
import pprint
import requests
import pandas as pd
import numpy as np
import csv
from pyproj import Proj, transform



class geoMongo:
    #toConnect
    client = MongoClient('localhost',27017)
    #define which db you're going to use
    db = client.district
    # UTM-K
    proj_UTMK = Proj(init='epsg:5178')
    # WGS1984
    proj_WGS84 = Proj(init='epsg:4326')


    def insert(self,col,name,geometry):
        co = col
        co.insert_one({"name":name,"geometry":geometry})

    def lst_of_amdcd(self):
        df = pd.read_csv('c://encore_migo/py_workspace/data/adm_code.csv',header=1)
        neiborhood = df[['읍면동명칭','읍면동코드']]
        with open('./writings/amdcd.csv','w',encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            header = ['읍면동명','코드']
            csv_writer.writerow(header)
            for i, j in zip(neiborhood['읍면동명칭'], neiborhood['읍면동코드']):
                csv_writer.writerow((i,j))


    def SGIS(self,adm_cd):
        api_url = "https://sgisapi.kostat.go.kr/OpenAPI3/boundary/hadmarea.geojson"
        params =f"?accessToken=97f60c4b-967d-4fbf-9bfe-293508fa11d3&year=2019&adm_cd={adm_cd}"
        url_request= requests.get(api_url+params).json()

        if url_request['errMsg'] == "검색결과가 존재하지 않습니다.":
            return None

        geo = url_request['features'][0]['geometry']['coordinates']

        #Multypolygon인 경우 4차원 배열을 갖으므로, 따로따로 해주어야 한다.
        if url_request['features'][0]['geometry']['type'] == "MultiPolygon":
            for i in range(len(geo)):
                df = pd.DataFrame(geo[i][0])
                df.columns = ['x', 'y']
                df['coor_xy'] = df.apply(self.getXY, axis=1)
                df.drop(axis=1, columns=['x', 'y'], inplace=True)
                df['x'] = df['coor_xy'].str.split(',').str[0]
                df['y'] = df['coor_xy'].str.split(',').str[1]
                df.drop(axis=1, columns='coor_xy', inplace=True)
                df['x'] = df['x'].astype('float64')
                df['y'] = df['y'].astype('float64')

                #업데이트
                geo[i][0] = list(map(list, df[['x', 'y']].values))
            else:
                return url_request['features'][0]['properties']['adm_nm'], url_request['features'][0]['geometry']

        else:
            df = pd.DataFrame(geo[0])


            df.columns = ['x','y']
            df['coor_xy'] = df.apply(self.getXY,axis=1)
            df.drop(axis=1,columns=['x','y'],inplace=True)
            df['x'] = df['coor_xy'].str.split(',').str[0]
            df['y'] = df['coor_xy'].str.split(',').str[1]
            df.drop(axis=1,columns='coor_xy',inplace=True)
            df['x'] = df['x'].astype('float64')
            df['y'] = df['y'].astype('float64')
            geo[0] = list(map(list,df[['x','y']].values))

            # 로케이션,이름 추출
            geometry = url_request['features'][0]['geometry']
            name = url_request['features'][0]['properties']['adm_nm']

            return name, geometry



    # 통계청 자료는 UTM-K로 되어있다! 그러나 몽고디비는 WGS-84만 취급할수있으므로 변환하여준다.
    def getXY(self,df):
        x1,y1 = df.x , df.y
        #UTM-K -> WGS84 만들기
        x2,y2 = transform(self.proj_UTMK,self.proj_WGS84,x1,y1)
        return f"{x2},{y2}"


    def create_neiborhood(self):
        co = self.db.neiborhood

        amd_df = pd.read_csv('./writings/amdcd.csv',encoding='utf-8')
        extract_code = amd_df['코드'].values
        failure = []
        for code in extract_code:
            if self.SGIS(code):
                name, geometry = self.SGIS(code)
                try:
                    self.insert(co,name,geometry)
                except:
                    failure.append([name,geometry])
        with open("./writings/fail_list.csv",'w',encoding='utf-8') as f:
            csv_writer = csv.writer(f)
            for i in failure:
                csv_writer.writerow(i)


if __name__ == '__main__':
    db = geoMongo()
    db.create_neiborhood()






