name='malayalai'
rev=''
for ch in range(len(name)):
    print(name[ch],name[len(name)-(ch+1)])
    rev=rev+name[len(name)-(ch+1)]
print('after reverse',rev)

if name==rev:
    print("palindrome")
else:
    print("not a palindrome")
