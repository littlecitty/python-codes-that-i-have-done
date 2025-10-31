#15. Sum of digits of a number.

num = int(input("enter a no. :"))
a=num
z=0
while num > 0:
   b=num % 10
   z += b
   num //= 10

print(f"the input no. is {a} sum of digits of {a} is {z}")
