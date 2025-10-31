#35. Sort a list using bubble sort.
a=list(map(int,input("enter integers seperated with ','. :").strip().split(",")))
b=len(a)

for i in range(b-1):
    for j in range(b-i-1):
        if a[j]>a[j+1]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)



#Optimized Bubble Sort (stop early if sorted)
a = list(map(int, input("Enter integers separated with ',': ").strip().split(",")))
b = len(a)

for i in range(b - 1):
    swapped = False
    for j in range(b - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
            swapped = True
    if not swapped:  # No swaps in this pass → already sorted
        break

print(a)



#Most Pythonic Way
a = list(map(int, input("Enter integers separated with ',': ").strip().split(",")))
a.sort()
print(a)

#or

a = sorted(map(int, input("Enter integers separated with ',': ").strip().split(",")))
print(a)

