# 36. Find common elements in two lists.
a = list(input("Enter elements for a: ").strip().split(","))
b = list(input("Enter elements for b: ").strip().split(","))

for element in a:
    if element in b:
        print(f"Common element: {element}")



#pythonic
a = list(input("Enter elements for a: ").strip().split(","))
b = list(input("Enter elements for b: ").strip().split(","))

common = set(a) & set(b)  # intersection of two sets

print("Common elements are:", ", ".join(common))

