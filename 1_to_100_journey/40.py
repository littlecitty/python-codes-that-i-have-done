# 40. Find second largest number in list.
#simple method  with sorting
a = list(map(int, input("Enter list of numbers: ").split(",")))
a.sort(reverse=True)  # Sort in descending order
print("Second largest number is:", a[1])



#Without Sorting (Better Logic)
a = list(map(int, input("Enter list of numbers: ").split(",")))

largest = second_largest = float('-inf')  # Start with smallest possible number

for num in a:
    if num > largest:
        second_largest = largest
        largest = num
    elif largest > num > second_largest:
        second_largest = num

print("Second largest number is:", second_largest)



#Pythonic one-liner
print(sorted(set(map(int, input("Enter list: ").split(","))))[-2])

# How it works:
# map(int, input().split(",")) → Converts input to integers.
# set(...) → Removes duplicates.
# sorted(...) → Sorts ascending.
# [-2] → Picks the second last element (second largest).
