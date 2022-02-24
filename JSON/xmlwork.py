import requests
import xmltodict
data_re = requests.get('http://10.47.25.51/getResources.xml').text
data_dict = xmltodict.parse(data_re)
sub_val = data_dict['response']['resource']
print(type(sub_val))
f = open("datadump.txt", "w+")
for i in sub_val:
    print(i['resourceName'], "and ", i['agentState'].get('pingToken', "empty"), file=f )
