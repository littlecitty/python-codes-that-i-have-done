# 46. Write to a file.
 
text=input("enter some thing to write on a file : ")

with open('rough.py','w') as file:
    file.write(text)

#pythonic
with open('rough.py', 'w') as f: f.write(input("enter some thing : "))
