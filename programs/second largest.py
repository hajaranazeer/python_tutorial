#to find the second largest among three numbers
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
n3=int(input("enter the third number"))
if((n1>n2) and (n1<n3))or((n1<n2) and (n1>n3)):
     print("second largest=n1",n1)
elif((n2>n1)and(n2<n3)) or ((n2<n1)and(n2>n3)):
     print("second largest=n2",n2)
else:#((n3>n1)and (n3<n2)) or ((n3<n1)and(n3>n2)):
     print("secondlargest=n3",n3)