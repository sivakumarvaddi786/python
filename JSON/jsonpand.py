import json
import pandas as pd
f = open('C:\\Users\\sivavadd\\VSPY\\JSON\\doc1.json', 'r')
data1 = json.loads(f.read())
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 1000)
pd.set_option('max_colwidth', 8000)
data = pd.json_normalize(data1)
NoneType = type(None)
for i , j in data1.items():
    if print(data1.get(i)):
        print(data)
        if type(j) == str:
            print(i, j)
            print()    
        elif type(j) == list:
            for x, z in j.items():
                print(x, "and", z)
            print()
        else :
            pass

    