#20. Count vowels in a string.
a = 0
text = input("enter a string. :")
text = text.lower()
chars = list(text) #list funtion is not necessary as all string are taken as list in line 7
for i in chars:
    if i in 'aeiou':
        a += 1
print(f"no. of vowels present in string is :{a}")
