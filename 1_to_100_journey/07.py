#check if a number is prime.
var1 = int(input("enter a no. :"))
i=1
a=0
while i <= var1:
    if var1 % i == 0:
        a+= 1
    i+=1

if a == 2:
    print(f"the no {var1} is prime")
elif var1 == 1:
    print(f"no should be > then 1")
    
