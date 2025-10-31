# 63. Use `reduce()` to calculate product of list.

from functools import reduce

class Outp:
    def __init__(self, *args):
        self.args = args

    def combine(self):
        return reduce(lambda x, y: x + " " + y, self.args)

class Gett(Outp):
    def gett(self):
        print(f"The thing you typed is:\n{super().combine()}")

def user():
    args = tuple(x.strip() for x in input("Enter string separated with ',' like: earth,for,humans : ").split(','))
    obj = Gett(*args)
    obj.gett()

user()



#short to demostrate for inntegers
args=tuple(map(int,input("enter integers seperated with ',': ").split(',')))
a=reduce(lambda x,y: x*y,args)
print(f"the multiplication of the given no is:{a}")
