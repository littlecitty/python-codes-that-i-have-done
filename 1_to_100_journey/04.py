#swap two variables.

a = int(input("ente 1st no. :"))
b = int(input("ente 2nd no. :"))

print(f"first variable is :{a} second variable is  :{b}") 
a = a ^ b
b = a ^ b
a = a ^ b
print(f"first variable is :{a} second variable is  :{b}") 
