#find the largest of three no.

a,b,c=map(int,input("enter 3 no. seperate with comas :").split(","))

if a>b and a>c: #use and instead of & . & is bitwise and in python
    print(f"{a} is the gretest")
elif b>a and b>c:
    print(f"{b} is the gretest")
else:
    print(f"{c} is the gretest")


#👉 How It Works:
#input() → gets string like "1 2 3"
#.split() → splits into ['1', '2', '3']
#map(int, ...) → converts each string to int
#a, b, c = ... → unpacks values into 3 variables



#list comprehension
#a, b, c = [int(x) for x in input("Enter 3 numbers with commas: ").split(",")]
#more clean
