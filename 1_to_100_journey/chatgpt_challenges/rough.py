class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l*self.b

    def perimeter(self):
        return 2*(self.l+self.b)

class Square(Rectangle):
    def __init__(self,side):
        super().__init__(side,side)

    def calc(self):
        return super().area()

    def perimeter(self):
        return (4 * self.l)

def user():
    l=int(input("enter length: "))
    b=int(input("enter breadth: "))
    rec=Rectangle(l,b)
    print(f"the area of rectangle is: {rec.area()}")
    print(f"the perimeter of rectangle is: {rec.perimeter()}")

    side=int(input("enter side: "))
    squ=Square(side)
    print(f"the area of square is: {squ.calc()}")
    print(f"the perimeter of square is: {squ.perimeter()}")

user()



