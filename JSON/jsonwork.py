import json
import requests
import xmltodict

data = requests.get('http://10.47.25.51/getResources.xml')
dict_data = xmltodict.parse(data.content)
#print(dict_data)
print(type(dict_data))
data_json = json.dumps(dict_data, indent=2)
print(type(data_json))


