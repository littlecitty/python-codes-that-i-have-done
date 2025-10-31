#25. Count frequency of characters.

strings = input("enter string. :")
counter={} # creates empty dictionary

for char in strings:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] =  1

print(counter)
