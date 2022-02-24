b = []
print('#' * 200)
tuple1 = [1, 2, 3, 'a', 'b', (4, 5, 6), [10, 20, 70, 50]]
for i in tuple1:
    if type(i) == int or type(i) == str:
          b.append(i) 
    else :
        for x in i:
          b.append(x)
        
print("unpacked list is: ",b)
print("length of the list is", len(b))

print('#' * 200)

        
