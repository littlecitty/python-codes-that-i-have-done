def two_sum(nums,target):
    seen={}
    for i,num in enumerate(nums):
        diff=target-num
        if diff in seen:
            return [seen[diff],i]
        seen[num]=i
nums=list(map(int,input("enter a list of no.: ").split(',')))
target=int(input("enter an integer.: "))
print(two_sum(nums,target))
