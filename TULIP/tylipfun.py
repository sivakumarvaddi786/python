b = []
print('#' * 200)
tuple1 = [1, 2, 3, (4, 5, 6), [10, 20, 70, 50]]
for i in range(len(tuple1)):
    a = tuple1[i]
    if type(a) == int:
          b.append(a)
    else :
        for x in range(len(a)):
            b.append(a[x])
        
print(b)
print('#' * 200)

        
