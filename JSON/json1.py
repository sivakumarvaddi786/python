import json
from unicodedata import name
people_string = {
    "people": [
        {
            "name": "sivkumar",
            "age":  32,
            "sex":  "Male",
            "hobbies": [ "reading", "gardening", "movies" ]
        },
        {
            "name": "prathyusha",
            "age":  28,
            "sex":  "Female",
            "hobbies": [ "reading", "gardening", "serials" ]
        }
     ]   
}
a = []    
def calculate_users(x):
    count = 0
    for i in x['people']:
        if i['age'] > 30:
            print("My Name is ", i['name'], "and my age is :", i['age'] )
        count += 1
        a.append(i['name'])
    print(count)
    print(a)
        


#calculate_users(people_string)

def check_hobbies():
    people_list = people_string['people']
    for i in people_list:
        print("Hobbies of ", i['name'] ,"is ", *i['hobbies'])
check_hobbies()