# 57. Use `super()` in inheritance.

class Parent:
    def __init__(self,l,b):
        self.l=l
        self.b=b

    def values(self):
        print(f"lenght:{self.l}, breadth:{self.b}:")

    def get(self):
        return (self.l*self.b)

class Child(Parent):
    def __init__(self,l,b):
        self.l=l
        self.b=b

        super().__init__(l,b)

    def calc(self):
        print(f"the Area is: {super().get()}")



def user():
    l=int(input("enter lenght: "))
    b=int(input("enter breadth: "))
    obj=Child(l,b)
    obj.values()
    obj.calc()

user()
