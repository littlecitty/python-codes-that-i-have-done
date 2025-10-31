#22. Check if a string is palindrome.

string = input("enter string. :")
a=""
b=int(len(string))
b-=1
while b >= 0:
    a+=string[b]
    b-=1
if string == a:
    print(f"the string is palindrome :{string}")
else:
    print(f"the string is not palindrome :{string}")

#using slicing
string = input("enter string. :")
b=string[::-1]
if string == b:
    print(f"the string is palindrome :{string}")
else:
    print(f"the string is not palindrome :{string}")

# Method 1: Manual reversal using loop (logic-based)
# Method 2: Pythonic slicing method

