# 58. Create and raise custom exception.
class InvalidDimensionError(Exception):
    """Custom exception for invalid dimensions"""
    pass


class Area:
    def __init__(self, l, b):
        if l <= 0 or b <= 0:
            raise InvalidDimensionError("Length and breadth must be positive numbers.")
        self.l = l
        self.b = b

    def cal(self):
        return self.l * self.b


class Rectangle(Area):
    def area(self):
        print(f"The area of rectangle is: {super().cal()}")


def user():
    try:
        l = int(input("Enter length: "))
        b = int(input("Enter breadth: "))
        obj = Rectangle(l, b)   # may raise InvalidDimensionError
        obj.area()

    except ValueError:
        print("❌ Please enter integers only.")
    except InvalidDimensionError as e:
        print(f"❌ Custom Error: {e}")


user()

