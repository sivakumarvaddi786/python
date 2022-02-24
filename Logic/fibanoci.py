num = 8
count = 0
a , b = 0 , 1
while count < num:
    print(a)
    c = a + b
    a = b
    b = c
    count += 1
