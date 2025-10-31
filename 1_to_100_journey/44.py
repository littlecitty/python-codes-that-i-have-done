# 44. Find most frequent character in string.
a = input("Enter a string: ").replace(' ', '').lower()

b = {}  # Dictionary to count characters

for i in a:
    b[i] = b.get(i, 0) + 1

# Now find the most frequent character
max_char = ""
max_count = 0

for char, count in b.items():
    if count > max_count:
        max_count = count
        max_char = char

print("Most frequent character:", max_char)
print("Frequency:", max_count)

