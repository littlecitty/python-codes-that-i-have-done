#27. Find sum of elements in list.

sum_list=list(map(int,input("enter list of integers. :").split(",")))
total=0
for i in sum_list:
    total+=i

print(total)

#pythonic way
# sum_boy=list(map(int,input("enter list of no.'s. :").split(",")))
# print(f"the sum of list is :{sum(sum_boy)}")

