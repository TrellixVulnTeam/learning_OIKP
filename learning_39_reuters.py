import urllib.request
from urllib.parse import quote_plus
import requests
from pprint import pprint
from bs4 import BeautifulSoup as bs
import csv

def top15():
    url = "https://www.reuters.com/pf/api/v3/content/fetch/articles-by-section-alias-or-id-v1?query=%7B%22fetch_type%22%3A%22section%22%2C%22id%22%3A%22%2Fworld%22%2C%22size%22%3A15%2C%22website%22%3A%22reuters%22%7D&d=39&_website=reuters"
    headers = {'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")}
    url_r = requests.get(url,headers=headers)
    list_article = url_r.json()['result']['articles']
    articles=[]
    with open("files/article_url.csv",'w',encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for i in list_article:
            title = i['title']
            art_url = "https://www.reuters.com" +i['canonical_url']
            updated_time =i['updated_time']
            decription = i['description']
            author = i['authors'][0]['name']
            articles.extend([title,art_url,updated_time,decription,author])
            f.write(art_url+"\n")


def soup():
    with open("files/article_url.csv",'r',encoding='utf-8') as f:
        for i in f.readlines():
            url = requests.get(i,headers={'User-Agent':("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36")})

            url_r = urllib.request.urlopen(i)
            print(url_r)
            soup = bs(url_r,'html.parser')

            for j in soup.find_all('h1',class_='Text__text___3eVx1j Text__dark-grey___AS2I_p Text__medium___1ocDap Text__heading_2___sUlNJP Heading__base___1dDlXY Heading__heading_2___3f_bIW'):
                print(j.text)
