import urllib.request
from urllib import parse
from bs4 import BeautifulSoup


def bsoup(search,ran1,ran2):
    korean_path = parse.urlparse(f"""https://search.naver.com/search.naver?where=image&section=image&query={search}&res_fr=0&res_to=0&sm=tab_opt&color=&ccl=0&nso=so%3Ar%2Cp%3Afrom{ran1}to{ran2}&recent=0&datetype=6&startdate=2021.06.03&enddate=2021.06.07&gif=0&optStr=d&nso_open=1""")
    query = parse.parse_qs(korean_path.query)
    result = parse.urlencode(query, doseq=True)
    path = f"""https://search.naver.com/search.naver?""" + result
    url = urllib.request.urlopen(path).read().decode('utf-8')


    soup = BeautifulSoup(url, "lxml").find_all('div')

    print(soup)

bsoup('사과',20200603,20200607)