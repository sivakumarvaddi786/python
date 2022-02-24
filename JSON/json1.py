import json
people_string = '''
{
    "people": [
        {
            "name": "sivkumar",
            "age":  "32",
            "sex":  "Male"
        },
        {
            "name": "prathyusha",
            "age":  "28",
            "sex":  "Female"
        }
     ]   
}
'''
a = []
#print(people_string)
print(type(people_string))
data = json.loads(people_string)
print(data)
print(type(data))
data1 = data['people']
print(type(data1))
for data2 in data1:
    print(data2['name'])
    a.append(data2['name'])
print(a)
    


