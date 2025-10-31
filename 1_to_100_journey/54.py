# 54. Create a class with method to calculate area of rectangle.
class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def calc_area(self):
        return self.length * self.breadth

def user():
    length = float(input("Enter length of rectangle: "))
    breadth = float(input("Enter breadth of rectangle: "))
    rect = Rectangle(length, breadth)
    print(f"The area of the rectangle is: {rect.calc_area()}")

user()



#pythonic
print("Area:", (lambda l, b: l * b)(float(input("Length: ")), float(input("Breadth: "))))

