#Focus: recursion, decorators, algorithms, regular expressions, multithreading
# 71. Implement binary search.
def binary_search(arr, target):
    left,right=0,len(arr)-1

    while left<=right:
        mid=(left+right)//2

        if arr[mid]==target:
            print( mid)
        elif arr[mid]<target:
            left=mid+1
        else:
            right=mid-1

    return -1

arr=[1,2,3,4,5,6,7,8,9,0]
target=input("enter no. 1-0 :")
binary_search(arr,target)
