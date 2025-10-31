#33. Create a function to return factorial.
import math
def function_(num):
    return math.factorial(num)
num = int(input("enter a no. :"))
print(f"the factorial is {function_(num)}")

#fixed version(recursive factorial)
def function_(num):
    if num == 0 or num == 1:
        return 1
    return num * function_(num - 1)

num = int(input("Enter a number: "))
print(f"Factorial of {num} is {function_(num)}")

