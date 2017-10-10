import xmltodict

def processXML(filename):
    with open('magazijn.xml') as myXMLFile:
        filestring = myXMLFile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary

artikelendict = processXML('magazijn.xml')
artikelen = artikelendict['artikelen']['artikel']

print(artikelendict)

for artikel in artikelen:
    print(artikel['naam'])
