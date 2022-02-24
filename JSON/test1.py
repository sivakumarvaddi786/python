import json

uglyjson = '{"firstnam":"James","surname":"Bond","mobile":["007-700-007","001-007-007-0007"]}'
data_dict = json.loads(uglyjson)
print(data_dict['firstnam'])

