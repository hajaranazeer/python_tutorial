class  Introclass:


    no=100
    def a(self):
        no=150
    print(no)

    def b(self):
        no=200
        self.no=250
    print(Intro.no)
    print(self.no)
    print(no)



obj=Intro()
obj.a()
print(obj.no)
print(obj.getname())