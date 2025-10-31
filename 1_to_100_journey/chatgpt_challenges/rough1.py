class Parent():
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

class Child(Parent):
    def __init__(self,side):
        self.side=side

        super().__init__(side,side)

    def area(self):
        return self.l**2

    def square(self):
        print(f"the area of square is: {self.area()}")

def user():
    l=int(input("enter lenght: "))
    b=int(input("enter breadth: "))
    rec=Parent(l,b)
    print(f"the area of rectangle is: {rec.area()}")

    side=int(input("enter side: "))
    squ=Child(side)
    squ.square()

user()

