import xml.etree.ElementTree as et   #파이썬 모듈
from collections.abc import Iterable
def Test():
    friend = et.parse('files/myfriend.xml')
    friends = friend.findall("address")
    for res in friends :
        print(res.find("name").text , ",",res.find("addr").text)

    print('============================')

def Test01():
    tree = et.ElementTree(file='files/fruit.xml') #파일로 불러오기.
    root =tree.getroot() #루트 주소 잡고

    for child in root:
        print("tag:", child.tag,
              "attributes:", child.attrib)  #갑자기 축약어?
        for grandchild in child:
            if grandchild.text != None:
                print("\ttag:",grandchild.tag, grandchild.text,
                    "attributes:",grandchild.attrib)
            else:
                print("\ttag:", grandchild.tag,
                      "attributes:", grandchild.attrib)

if __name__ == '__main__':
    Test()


#과일, 야채 분류 가격분류