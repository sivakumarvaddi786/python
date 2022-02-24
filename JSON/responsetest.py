from urllib import response
import requests
import json
import warnings
warnings.warn('my warning')
r = requests.get('https://qso-linttest.qualcomm.com:8443/rest/v1.0/resources', auth=('sivavadd', 'Hello@Kitty'), verify=False)
print(r.status_code)
#print(r.text)
print(type(r.text))
json_data = r.json()
print('#' * 200)
#print(json_data)
for i, j in json_data.items():
    for x  in j:
        #print(x)
        print(x['resourceName'])
