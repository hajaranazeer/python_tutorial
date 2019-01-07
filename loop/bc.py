n=8
for i in range(n,0,-1):
    for j in range(n-i):
     n=n-1
     print(j,end='')
    print()
    for j in range(i):
        print( j,end='')
    print()