#print all prime no. in a range

var1 = int(input("enter a no till you want to print prime no. :"))
i = 1
for a in range(i+1, var1):
    if a > 1:
        for j in range(2, a):
            if ( a % j) ==  0:
                break
        else:
            print(a)



#chatgpt version clean and tity@s   
var1 = int(input("enter a no till you want to print prime no. :"))
for a in range(2, var1):
    for j in range(2, int(a ** 0.5) + 1):
        if a % j == 0:
            break
    else:
        print(a)

