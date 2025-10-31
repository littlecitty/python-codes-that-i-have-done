# 60. Create a lambda function.

class Area:
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs

    def cal(self):
        multiply= lambda nums: __import__('functools').reduce(lambda x,y:x*y,nums,1)
        return multiply(self.args)
    
    def key(self):
        return self.kwargs

class Rectangle(Area):
    def area(self):
        print(f"the area of Rectangle: {super().cal()}")
        print(" | ".join(f"{k}:{v}" for k,v in super().key().items()))

def user():
    raw=input("enter length, breadth as lenght=4,breadth=2: ")
    kwargs={k: int(v) for k,v in (item.split('=') for item in raw.split(','))}
    args=tuple(kwargs.values())

    obj=Rectangle(*args,**kwargs)
    obj.area()

user()


