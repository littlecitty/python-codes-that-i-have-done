# 65. Use list comprehension to square numbers.

def cal():
    no = list(map(int, input("enter list of no. like: 1,2: ").split(',')))
    squared = list(map(lambda x: x**2, no))   # lambda replaces the comprehension
    print(squared)

cal()

