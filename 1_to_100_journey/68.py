# 68. Use `enumerate()` in loop.

fruits = ['apple', 'banana', 'cherry']
for index, fruit in enumerate(fruits):
    print(index, fruit)

class Enumerate:
    def __init__(self,fruits):
        self.fruits=fruits

    def cal(self):
        for fruit in self.fruits:
            yield (fruit)

class Getter(Enumerate):
    def getter(self):
        print("the fruits are: ")
        for index,v in enumerate(self.cal()):
            print(index,v)

def User():
    fruits=list(input("enter fruits seperated with ',': ").split(','))

    obj=Getter(fruits)
    obj.getter()

User()

    
