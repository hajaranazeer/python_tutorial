nos= [5,6,7,8,9]
nos.append(1.2)

for i in nos:
    print(i)

nos.remove(5)
print(nos)

print(sum(nos))

for i in reversed (nos):
    print(i)

rev=list(reversed(nos))
print(rev)

asc=list(sorted(nos))
print(asc)

for i in searched(nos(2)):
    print(i)

desc=list(reversed(asc))
print(desc)

print("no of elements=",len(desc))

asc.append(8)
print(asc)
print("no of 1=",asc.count(8))
