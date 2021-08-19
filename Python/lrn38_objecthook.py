import json

from pandas.conftest import datapath


class TEST:
    def __init__(self,data):
        self.__dict__ = data

def prn():
    f = open('../files/b.json','r')
    str = f.read()
    f.close()

    data = json.loads(str,object_hook=TEST)   #json.loads로 파일의 객체를 넣고자 할 때.
    for my in data.result: #데이터 객체의 키 = STUDENT.  그 키의 밸류 = list 형태. 그러므로 iterable.
        print(data.DEPTNO)
#안에 있는 keys, values를 모른다고 가정해볼때, 어떻게 값을 얻어올까?


if __name__ == '__main__':
    prn()