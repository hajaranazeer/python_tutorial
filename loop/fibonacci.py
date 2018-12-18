n=int(input("enter how many nos "))

a=0
b=1
print(a,"\t",b,"\t")

for i in range(n):
    next=a+b
    print(next)
    a=b
    b=next
