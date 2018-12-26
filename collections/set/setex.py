#it is unordered and un indexed. cannot contain duplicate elements

nos={1,2,3,4,5}
for x in nos:
    print(x)

nos.add(5);
nos.add(6);
nos.add(8);
print(nos)
nos.remove(4)
print(nos)
asc=set(sorted(nos))
print(asc)
print("no of elements=",len(asc))
asc.add(10)
print(asc)

