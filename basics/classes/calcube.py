from basics.classes.calcube import calculate
class CalCube(Calculate):
    name="base2_mariam"
    def __init__(self):
        print("i am initialized in CalCube and calculating cube")

    def cube(self,n):
        return n**3;

c=CalCube()
print(c.cube(3))
print(c.square(3))