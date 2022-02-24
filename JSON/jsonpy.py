import json
f = open('C:\\Users\\sivavadd\\VSPY\\JSON\\docker.json')
data = json.load(f)
print(type(data))
for i in data:
    print(i)
    print('*' * 150)
    print('*' * 150)
    for x in i:
        print(type(i[x]))
