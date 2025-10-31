#simple version:
def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                return [i,j]
nums=list(map(int,input("enter list of numbers separated by commas: ").split(',')))
target=int(input("enter target sum: "))

print(two_sum(nums,target))




#Optimized Hash Map Version:
def two_sum(nums, target):
    seen = {}  # stores {number: index}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff], i]  # found the pair
        seen[num] = i  # store the current number and its index

nums = list(map(int, input("Enter list of numbers separated by commas: ").split(',')))
target = int(input("Enter target sum: "))

print(two_sum(nums, target))

