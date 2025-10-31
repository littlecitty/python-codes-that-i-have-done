#43. Check if two strings are anagrams.
a=input("enter a string : ").lower()
b=input("enter a string : ").lower()
if sorted(a) == sorted(b):
    print("the string are anagrams ")
else:
    print("the string are not anagrams")



