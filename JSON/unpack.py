def unpack_list(list):
    for i in list:
        print(i)

def unpack_dict(dict):
    if dict:
        for i, j in dict.items():
            if type(j) == str or type(j) == str:
                print(j)
            elif type(j) == list or type(j) == tuple:
                unpack_list(j)
            else :
                unpack_dict(j)
                
def check_type(data_type):
        if type(data_type) == dict:
            unpack_dict(data_type)
        else  :
            unpack_list(data_type)

lisst1 = [1, 2, 3, 4, 5]
lisst2 = (1, 2, 3, 4, 5)
lisst4 = {1, 2, 3, 4, 5}
lisst3 = { "name": "siva", "place": { "name": "kakinada", "place": { "name": "Hyd", "place": "sing" } }, "age": ("Female", "Male"), "sex": [1, 2, 3, 4] }
#unpack_list(lisst1)
#unpack_list(lisst2[::-1])
#unpack_list(lisst4)
#unpack_dic(lisst3['place'])
check_type(lisst3)