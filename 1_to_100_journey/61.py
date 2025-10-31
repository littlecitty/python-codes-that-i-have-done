# 61. Use `map()` with lambda.

class Area:
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs

    def cal(self):
        multiply=lambda nums: __import__('functools').reduce(lambda x,y:x*y,nums,1)
        return multiply(self.args)

    def key(self):
        return self.kwargs

class Rectangle(Area):
    def area(self):
        print(f"the area of rectangle is: {super().cal()}")
        print(" | ".join(f"{k}:{v}" for k,v in super().key().items()))

def user():
    raw=input("enter lenght & breadth as length=10,breadth=20: ")
    kwargs=dict(map(lambda items: (items.split("=")[0], int(items.split("=")[1])),raw.split(",")))
    args=tuple(kwargs.values())

    obj=Rectangle(*args,**kwargs)
    obj.area()

user()
