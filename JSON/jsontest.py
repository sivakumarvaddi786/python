import xmltodict
import json
import warnings
warnings.warn('my warning')
with open('C:\\tmp\\qsoec-linttest10-task01.xml', 'r') as f:
        data = xmltodict.parse(f.read())
print(data['response']['resource']['resourceName'])

data_json = json.dumps(data, indent=2)
del data['response']['resource']['resourceName']
print(data_json)

