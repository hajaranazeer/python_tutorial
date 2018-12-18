#sum of first n nos

n=int(input("enter n value"))

nos=range(n+1)
sum=0
for i in nos:
    sum=sum+i
print("sum of ",n," nos = ",sum)
