#23. Replace a word in a sentence.

sentence= input("enter a sentence : ")

print(sentence)
print("what string do you want to replace from above sentence.")
old_string,new_string=input("enter old and new string seperated with comma : ").split(", ")
sentence=sentence.replace(old_string,new_string)
print(sentence)

