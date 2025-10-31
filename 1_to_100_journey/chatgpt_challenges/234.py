class Rectangle:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b


class Square(Rectangle):  # ✅ Inherit from Rectangle
    def __init__(self, side):
        # Square is just Rectangle with l = b = side
        super().__init__(side, side)

    def area(self):
        print("Calculating Square Area...")
        return super().area()   # ✅ call parent's area()

    def calc(self):
        print(f"The area is: {self.area()}")


def user():
    l = int(input("Enter length: "))
    b = int(input("Enter breadth: "))

    rect = Rectangle(l, b)
    print(f"Rectangle area: {rect.area()}")

    side = int(input("Enter side of square: "))
    sq = Square(side)
    sq.calc()


user()
