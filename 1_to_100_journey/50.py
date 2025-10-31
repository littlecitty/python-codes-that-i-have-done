# 50. Exception handling: divide by zero.
try:
    a = int(input("Enter a number: ").replace(' ', ''))
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Please enter a valid number.")



#pythoic
print((lambda x: 10/int(x.strip()))(input("Enter a number: ")) if input else None)

