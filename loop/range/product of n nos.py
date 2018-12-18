#product of n nos

n=int(input("enter n value"))

nos=range(1,n+1)
product =1
for i in nos:
    product=product*i
print("product of ",n," nos = ",product)
