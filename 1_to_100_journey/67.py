# 67. Write a generator for Fibonacci numbers.

class Numb:
    def __init__(self, num):
        self.num = num

    def cal(self):
        a, b = 0, 1
        for _ in range(self.num):
            yield a   # generator: gives one number at a time
            a, b = b, a + b

class UserNum(Numb):
    def princal(self):
        print("The Fibonacci numbers are:")
        for val in self.cal():   # iterate over the generator
            print(val)

def user():
    num = int(input("Enter number of Fibonacci terms: "))
    obj = UserNum(num)
    obj.princal()

user()

