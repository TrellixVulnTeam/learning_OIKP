import xml.etree.ElementTree as et

def XML():
    tree = et.ElementTree(file="files/Doit.xml")
    print(type(tree))
    root = tree.getroot()
    print(root.tag)
    for site in root.findall('site'): #> list
        print("\t\t"+site.tag)
        print("\t\t\t" + site.find('name').text)
        print("\t\t\t\t" +site.find('url').text)

XML()