student={
"name":"hajara",
"id":36,
"place":"padur",
    45:56,
"name":"hajara",
    }
print("student")
name=student["name"]
print(name)
str=student.get("place")
print(str)
student["place"]="ramnad"
print(student)
student["college"]="b.s.a.u"
print(student)
for x ,y in student.items():
  print(x,y)
if "id" in student:
    print(student.get("id",'is available'))
print(student)
student.popitem()
print("after pop",student)
student.pop("name")
print(student)







