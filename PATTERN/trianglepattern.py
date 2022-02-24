def Triangle(n):
    for i in range(0, n):
        for x in range(0, n-i):
            print(end = " ")
        for j in range(0, i+1):    
            print('*', end=" ")
        print()

Triangle(20)