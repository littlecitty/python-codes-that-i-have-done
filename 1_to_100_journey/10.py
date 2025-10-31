#calculate the factorial of a no.

num = int(input("enter a no: "))
b = 1
for i in range(1, num + 1):
    b *= i
print(f"the factorial : {b}")


