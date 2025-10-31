#check for armstrong number.

num = int(input("enter a no :"))
a=num
count = len(str(num))
b=0
while num > 0:
    num2 = num % 10
    num = num // 10 #123 // 10 equal to 12 no decimal
    b += (num2 ** count)

if a == b:
    print(f"the no. is armstrong aka: {b}")
else:
    print(f"the no. is not armstrong :( : {b}")


