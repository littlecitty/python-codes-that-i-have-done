#16. Check if a year is leap year.

num = int(input("enter a no. :"))

#the order should be there to work 400 to 4
if num % 400 == 0:
    print(f"the year is leap year {num}")
elif num % 100 == 0:
    print(f"the year is not leap year {num}")
elif num % 4 == 0:
    print(f"the year is leap year {num}")
else:
    print(f"the year is not leap year {num}")

