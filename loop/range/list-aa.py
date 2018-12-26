#[expression for(zero or more for or if)]
t=[]
t=[(n+1) for n in range(8)]
print(t)
for j in t:
    print(j)
nos=[1,2,3,4,5,6]
sq=[]
sq=[(each**2) for each in nos if each%2==0]
print(sq)


