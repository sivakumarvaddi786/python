data = [{ "name": "siva", "age": 20, "sex": "Male", "work": "IT", "email": "siva@test" }, { "name": "pratyu", "age": 10, "sex": "Female", "work": "HM", "email": "pratyu@test" }, { "name": "teja", "age": 25, "sex": "Male", "work": "IT", "email": ["teja@test", "teja@bonus"] } ]
print(type(data))
M = []
F = []
for i in data:
    if i['sex']  == "Male":
        M.append(i['name'])
    else:
        F.append(i['name'])
print("No of Male persons are", len(M))
print("No of FMale persons are", len(F))
print("Total users arr: ", len(M) + len(F) )

for i in range(len(data)):
    print("Name of user:", data[i]['name'], "and occupation is:", data[i]['work'] )