#sum of first n nos

n=int(input("enter n value"))

nos=range(1,(n+1))
fact=1
for i in nos:
    fact= fact * i
print("fact of ", n," nos = ", fact)
