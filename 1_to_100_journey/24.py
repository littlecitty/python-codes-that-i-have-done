#24. Remove punctuation from string.

import string

word = input("enter string. :")
renewed = ""
for i in word:
    if i not in string.punctuation:
        renewed+=i
print(f"the string without punctuation is: {renewed}")



#pythonic style
import string

text = "Hello, world!"
clean_text = ''.join(char for char in text if char not in string.punctuation)
print(clean_text)

# ✅ Line-by-Line Breakdown (Fixed Explanation):
# renewed = ""
# ✅ You got it right — creates an empty string to store the final cleaned text.
# 
# .join(...)
# ✅ You're right again! It takes all the characters generated from the loop and joins them into a single string — no spaces between, since we're using '' (empty string) as the separator.
# 
# i for i in word
# ✅ This is called a generator expression.
# 
# It means: "for each character i in the string word, give me i if the condition passes."
# 
# if i not in string.punctuation
# ✅ Spot on — this condition filters out all punctuation.
# 
# Only non-punctuation characters go into the final result.
