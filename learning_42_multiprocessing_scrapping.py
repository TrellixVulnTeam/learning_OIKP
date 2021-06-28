import requests
import multiprocessing
from bs4 import BeautifulSoup as bs
import csv
import time
from functools import partial #to put more than or equal to two variables.

def scrapping(file,number):
    url = f"""https://home.ebs.co.kr/ladybug/board/6/10059819/oneBoardList?c.page={number}&hmpMnuId=106&searchCondition=
    &searchConditionValue=0&searchKeywordValue=0&searchKeyword=&bbsId=10059819&"""
    a = requests.get(url).content
    soup = bs(a,'html.parser')

    with open(file,'a',encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for i in soup.find_all('li', class_="spot_"):
            id = i.find('span',class_="userid").get_text()
            comment = i.find('p',class_="con").get_text()
            csv_writer.writerow([id,comment])





if __name__ == '__main__':
    t1 = time.time()
    func = partial(scrapping,"writings/ladybug3.csv")
    #for i in range(1,23):
    #    scrapping("writings/ladybug2.csv",i) -> it takes 20 odds second.
    with multiprocessing.Pool(23) as p:
        p.map(func,range(1,23))
    t2 = time.time()
    print(f"time it takes : {t2-t1} seconds")