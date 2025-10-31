# 37. Merge two dictionaries.
# Example input for a: key1:val1,key2:val2
# Example input for b: key3:val3,key4:val4

a_input = input("Enter elements for a (key:value,key:value): ").strip()
b_input = input("Enter elements for b (key:value,key:value): ").strip()

# Convert input strings to dictionaries
a = dict(item.split(':') for item in a_input.split(','))
b = dict(item.split(':') for item in b_input.split(','))

# Merge
c = {**a, **b}  # Works for Python 3.5+
print(c)



#pythonic
# 37. Merge two dictionaries (short version)
a = dict(pair.split(':') for pair in input("a: ").split(','))
b = dict(pair.split(':') for pair in input("b: ").split(','))
print({**a, **b})  # Merges

