import xml.dom.minidom

def test():
    dom = xml.dom.minidom.parse("writings/Doit.xml")
    print(dom.documentElement.tagName) #태그네임
    #node객체로 접근해서 데이터 호출
    for node in dom.documentElement.childNodes: #자식노드
        if node.nodeType == node.ELEMENT_NODE:
            print(" "+ node.tagName)
            for node2 in node.childNodes:
                if node2.nodeType == node2.ELEMENT_NODE:
                    print(" "*10 + node2.tagName)
                    for node3 in node2.childNodes:
                        if node3.nodeType == node3.TEXT_NODE:
                            print(" "*20+ node3.data)
    print("-----------------------------------")
    for url in dom.getElementsByTagName("url"): #한번에 접근.
        print(url.firstChild.data)

test()
