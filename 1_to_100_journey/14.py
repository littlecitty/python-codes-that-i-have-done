#14. Print reverse of a number.

num = int(input("enter a no. :"))
a = num
e=0
while num > 0:
    d = num % 10
    e = e * 10 + d
    num = num // 10
print(f"the reverse of no. {a} is {e}")
