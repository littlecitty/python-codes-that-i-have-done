# 53. Create a class with constructor and destructor.
class Demo:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called! Name: {self.name}")

    def __del__(self):
        print("Destructor called! Object deleted.")

obj = Demo(input("enter name: "))
del obj

