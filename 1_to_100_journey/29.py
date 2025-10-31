#29. Check if an element exists in list.
import sys

text = list(input("enter strings. :").lower().split(","))
print(text)

elef = input("enter an element. :").lower()

# for element in text:
#     if element == elef:
#         print(f"the element exitst {elef}")
#         sys.exit()
#     else:
#         print(f"the element doesn't exit {elef}")

for  element in text:
    if element == elef:
        b = 0

if b == 0:print(f"the element exist {elef}")
else:print(f"the element doesn't exist {elef}")



#pythonic way
items = [s.strip() for s in input("Enter comma-separated values: ").lower().split(",")]
target = input("Search for: ").lower().strip()
print(f"{'✅ Found' if target in items else '❌ Not found'}: {target}")

