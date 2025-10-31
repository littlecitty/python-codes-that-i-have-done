# 47. Append to a file.
a=input("enter file path : ")

with open(a, 'a') as file:
    file.write(input("enter some thing that you want to append : ").strip() + '\n')

#pythonic
with open(input("enter file path :"), 'a') as f: f.write(input("write someting :") + '\n')
