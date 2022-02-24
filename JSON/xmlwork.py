import xml.etree.ElementTree as ET
import requests
import xmltodict
data_re = requests.get('http://10.47.25.51/getResources.xml').text
print(type(data_re))
data_dict = xmltodict.parse(data_re)
print(type(data_dict))
for i, j in data_dict.items():
    for x, y in j.items():
        #print(y)
        for a in y:
            #print(a)
            for  m  in a:
                for c, d in m.items():
                 print(c)
