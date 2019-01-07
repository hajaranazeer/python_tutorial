from functools import reduce

nos=range(1,11)
difference=reduce(lambda x,y:x-y, nos)
print(difference)