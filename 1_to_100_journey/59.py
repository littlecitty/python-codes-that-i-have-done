# 59. Use `*args` and `**kwargs` in function.
class Area:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def cal(self):
        a = 1
        for i in self.args:
            a *= i
        return a

    def key(self):
        return self.kwargs


class Rectangle(Area):
    def area(self):
        print(f"the area of rectangle is: {super().cal()}")
        print(f"enter length and breadth: {super().key()}")


def user():
    args = tuple(map(int, input("enter length and breadth separated by ',': ").split(',')))

    kwargs = {k: int(v) for k, v in (item.split('=') for item in input(
        "enter length=no, breadth=no: "
    ).split(','))}

    obj = Rectangle(*args, **kwargs)
    obj.area()


user()




#simplified
class Area:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def cal(self):
        a = 1
        for i in self.args:
            a *= i
        return a

    def key(self):
        return self.kwargs


class Rectangle(Area):
    def area(self):
        print(f"the area of rectangle is: {super().cal()}")
        print(f"length and breadth as kwargs: {super().key()}")


def user():
    # Single input like: "length=5,breadth=10"
    raw = input("Enter length and breadth like length=5,breadth=10: ")

    # Convert into kwargs
    kwargs = {k: int(v) for k, v in (item.split('=') for item in raw.split(','))}

    # args = only values of kwargs
    args = tuple(kwargs.values())

    obj = Rectangle(*args, **kwargs)
    obj.area()


user()

