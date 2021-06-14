import xml.etree.ElementTree as et
#https://docs.python.org/3/library/xml.etree.elementtree.html



def test():
    tree = et.ElementTree(file='writings/fruit.xml')
    root = tree.getroot()
    for basket02 in root.iter('basket'):
        if basket02.attrib['classification'] =='vegetable':
            print('\t (채소)', basket02.attrib['name'])
        else:
            print('\t (과일' , basket02.attrib['name'])

def test01():
    tree = et.ElementTree(file='writings/fruit.xml')
    root = tree.getroot()
    for origin in root.findall('origin'):
        if origin.attrib['name'] =='Andes': #origin의 name 속성값이 Andes라면
            origin.set('name', 'Canada') # 속성값 변경을 Canada로 지정  -> 영구적으로 적용은 어떻게 하나?
        quantity = int(origin.find('quantity').text)
        price = int(origin.find('price').text)
        if quantity<5: #수량 5 이하인 origin element삭제
            root.remove(origin)
        total = quantity * price
        for res in origin.findall('basket'):
            print(res.get('name'),format(total,',')) # this format function makes it 100,000,000

if __name__ == '__main__':
    test01()
