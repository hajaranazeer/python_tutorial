nos= [1,2,3,4,89,11,56]
nos.append(3.6)


for i in nos:
  print(i)

nos.remove(3)
print(nos)

print(sum(nos))

for i in reversed(nos):
  print(i)

rev=list(reversed(nos))
print(rev)

asc=list(sorted(nos))
print(asc)

desc=list(reversed(asc))
print(desc)

print("no of elements=",len(desc))
desc.append(1)
desc.append(1)
desc.append(1)
print(desc)
print("no of 1=",desc.count(1))