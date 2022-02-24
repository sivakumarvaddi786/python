from audioop import mul
from operator import contains


tup_set1 = ('a', 'b', 'c', 'd')
tup_set2 = (1, 2, 3, 4)
tup_set3 = tup_set1 + tup_set2
print(tup_set3)
tup_set4 = []
tup_set4 += [i for i in tup_set3]
print(tup_set4)
print(dir(tup_set4))
#print(dir(tup_set3))
#print(tup_set3 * 30)

print("a" in tup_set4)
#help(tup_set1.__contains__)
print(tup_set2.count(6), "times repaeted")
print(tup_set2.__dir__)

