#30. Remove duplicates from a list.

strg = [s.strip() for s in input("enter list of elements. :").lower().split(",")]
new={}
for a in strg:
    if a not in new:
        new[a] = True
print(new)



#pythonic
#method 1
strg = [s.strip() for s in input("Enter elements (comma-separated): ").lower().split(",")]
unique = list(dict.fromkeys(strg))  # Preserves order, removes duplicates
print("✅ Unique items:", unique)

#method 2
strg = [s.strip() for s in input("Enter elements: ").lower().split(",")]
unique = list(set(strg))  # Removes duplicates, but order is not guaranteed
print("✅ Unique items:", unique)

#hardcore pythonic
print(list(dict.fromkeys(s.strip() for s in input("enter string. :").lower().split(","))))

