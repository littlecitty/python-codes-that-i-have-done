#28. Find the max and min in list.
compare =list(map(int,input("enter list of integers split with , :").split(",")))
d = len(compare)
a=b=compare[0]
for i in range(1,d):
    if compare[i] >=a:
        a=compare[i]
    elif compare[i] <=b:
        b=compare[i]

print(f"the max value in list is {a} and min value in list is {b}")

#pythonic sytel
# compare=list(map(int,input("enter list of no. :").split(",")))
# print(f"max is {max(compare)} and min is {min(compare)}")
