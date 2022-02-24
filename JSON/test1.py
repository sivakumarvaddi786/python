import json

uglyjson = '{"firstnam":"James","surname":"Bond","mobile":["007-700-007","001-007-007-0007"]}'

#json.load method converts JSON string to Python Object
parsed = json.loads(uglyjson)
for x,y in parsed.items():
    print(y)
#print(json.dumps(parsed, indent=2, sort_keys=True))