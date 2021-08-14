from bs4 import BeautifulSoup as bs
from urllib import parse
import requests
import os


def basic_scrapping(search):
    url_request = requests.get("https://koreajoongangdaily.joins.com/section/searchResult/{}".format(parse.quote(search)))
    soup = bs(url_request.content,'html.parser')
    news = []
    for i in soup.find_all("div",class_="mid-article3"):
        new = i.find('a').get("href")
        news.append(new)
        print(new,type(new))
    with open('/root/test/scrap1.txt','wt',encoding='utf-8') as f:
        for j in news:
            url_request2 = requests.get(j).content
            soup2 = bs(url_request2,'html.parser')
            headline = soup2.find('div',id="article_body").h1.text.strip()
            f.write(headline )
            for k in soup2.find('div',id="article_body"):
                if str(type(k)) != "<class 'bs4.element.Tag'>":
                    print(k.strip())
                    f.write(k.strip()+"\r")

basic_scrapping("north korea") #만들고
try:
	os.system("$HADOOP_HOME/bin/hdfs dfs -put /root/test/scrap1.txt /testfolder") #올리고
	os.system("$HADOOP_HOME/bin/hadoop jar /root/test/wc.jar -Dwordcount.case.senstive=false /testfolder/scrap1.txt /testfolder/output/result1 -skip /testfolder/pattern.txt") #아웃풋 산출
	#os.system("$HADOOP_HOME/bin/hadoop jar /root/test/wc.jar /testfolder/scrap1.txt /testfolder/output/result1")
except:
	#os.system("$HADOOP_HOME/bin/hadoop jar /root/test/wc.jar /testfolder/scrap1.txt /testfolder/output/result1")
	os.system("$HADOOP_HOME/bin/hadoop jar /root/test/wc.jar -Dwordcount.case.senstive=false /testfolder/scrap1.txt /testfolder/output/result1 -skip /testfolder/pattern.txt")
finally:
	os.system("$HADOOP_HOME/bin/hdfs dfs -ls -R /testfolder/output")

