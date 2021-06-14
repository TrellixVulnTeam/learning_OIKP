from xml.dom.minidom import parse, parseString    #w3c module xmlhandling2에 있는 모듈보다 더 대중적.
#https://docs.python.org/3/library/xml.dom.minidom.html


dom = parse('writings/myfriend.xml') #임포트한 것을 가지고 파싱 - > 돔트리화
for name in dom.getElementsByTagName('name'):
    print(name.firstChild.data)

print('==============================================')
datasource = open('writings/myfriend.xml') #파일로 읽어와서 파싱한다.
dom2 = parse(datasource)
for name in dom.getElementsByTagName('addr'):
    print(name.firstChild.data)


