n=8
for i in range(8):
    for j in range(0,n):
        print( end = " ")
    n=n-1
    for j in range(0,i-1):
        print(j, end = " ")
    print()