# 56. Override a method in child class.

class Parent:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def given(self):
        print(f"the length:{self.length} and breadth:{self.breadth}")

    def grandson(self):
        print("Parent grandson method")


class Child(Parent):
    def grandson(self):  # overriding method
        print(f"Area is: {self.surprise()}")

    def surprise(self):
        return self.length * self.breadth


def user():
    length=int(input("enter length: "))
    breadth=int(input("enter breadth: "))
    holder=Child(length,breadth)

    holder.given()      # parent method
    holder.grandson()   # overridden child method

user()






















#my own lovely code :)
# class parent:
#     def __init__(self,length,breadth):
#         self.length=length
#         self.breadth=breadth
# 
#     def given(self):
#         print(f"the length:{self.length} and breadth:{self.breadth}")
# 
#     def grandson(self):
#         print(f"the output is: ")
# 
# class child(parent):
#     def grandson(self):
#         print(suprise(self))
# def user():
#     length=int(input("enter length: "))
#     breadth=int(input("enter breadth: "))
#     holder=child(length,breadth)
# 
#     holder.given()
#     holder.grandson()
# 
# def suprise(self):
#     return self.length*self.breadth
# user()
