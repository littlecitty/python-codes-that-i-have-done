#21. Reverse a string without slicing.

string = input("enter a string. :")
count = len(string)
gnirts=""
a=int(count-1)
print(count)
for i in range(1,count+1):
    gnirts+=string[a]
    a-=1
print(gnirts)
    
