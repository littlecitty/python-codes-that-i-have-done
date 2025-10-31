# 52. Create a class for student and display details.
class a:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def greet(self):
        print(f"your name is {self.name} and your age is {self.age}")

b={}
n=int(input("enter the no. of student you want to add: "))

for i in range(n):
    name=input(f"enter name of student {i+1}: ")
    age=input(f"enter age of student {i+1}: ")
    b[i+1]=a(name,age)

for a,c in b.items():
    print(a, end=" ");c.greet()


