#13. Check for palindrome number.

num = int(input("enter a no. :"))
copy = num
f=0
count = len(str(num))
while copy > 0:
    a = copy % 10
    copy = copy // 10
    f = f * 10 + a

if f == num:
    print(f"the no {num} is palindrome")
else:
    print(f"the no is not palindrome {num}")


