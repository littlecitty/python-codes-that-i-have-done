# 62. Use `filter()` to filter even numbers.

class Even:
    def __init__(self,no):
        self.no=no

    def give(self):
        return tuple(filter(lambda n: n%2==0 ,range(1,self.no+1)))

class Inp(Even):
    def outp(self):
        print(f"the output is: \n {super().give()}")

def user():
    no=int(input("enter no. till where you want even no.: "))

    obj=Inp(no)
    obj.outp()

user()
