from basics.classes.calsqr import calculate
from basics.classes.calcube import calculate
class Run(CalCube):

    def __init__(self):
        print(" i am intialised in run class ")
        Calculate.__init__(self) # to initialize in parent classes
        CalCube.__init__(self)

    def powerfour(self,no):
         return no**4

r=Run()
print(r.powerfour(3))
print(r.cube(3))
print(r.square(2))
print(r.name)
