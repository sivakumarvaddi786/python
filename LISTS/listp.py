str_1 = "siva is very good"
print(str_1)
print(str_1[4::-1])
print(len(str_1))
print("#################################################")
if len(str_1) == 1:
    print("yes we are good")
else :
    print("bad")
print("#################################################")

set1 = ['siva', 32, 'Ayan', 4] 
set2 = ["mom", 5, "dad", 55]
set2[3] = 60
set3 = set1 + set2
print(set3)
print("#################################################")
set_num = []
set_alp = []
for value in set3:
    print(value, "is", type(value))

print(set3[1] - set3[3])

for item in set3:
       if type(item) == int:
           set_num.append(item)
       else:
           set_alp.append(item)

print(set_alp)
print(set_num)
print(set_num)

number_set = [10, 2, 93, 45, 25]
print(sorted(number_set))

x = 0
sort_order = []

while number_set:
    minimum = number_set[0]
    for item in number_set:
        if item < minimum:
            minimum = item
    sort_order.append(minimum)
    number_set.remove(minimum)
print(sort_order)