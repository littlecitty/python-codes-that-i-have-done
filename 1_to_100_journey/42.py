# 42. Find pairs with sum in a list.
nums = [2, 4, 3, 5, 7, 8, 9, 5]
target = 10
pairs = set()

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):  # start from i+1 to avoid reverse duplicates
        if nums[i] + nums[j] == target:
            pairs.add(tuple(sorted((nums[i], nums[j]))))  # sorted to avoid (8,2) vs (2,8)

print(pairs)



#pythonic
nums = [2, 4, 3, 5, 7, 8, 9, 5]
target = 10
pairs = {(a, b) for i, a in enumerate(nums) for b in nums[i+1:] if a + b == target}
print(pairs)

