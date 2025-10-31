# 71. Implement binary search.

def binary_search(arr,left,right,target):
    #base case: if range is invalid then target not found
    if left > right:
        return -1

    #find the middle index
    mid = (left + right) // 2

    # case 1: target is exactly at mid
    if arr[mid]==target:
        return mid

    #case 2: Target is smaller then search in LEFT half
    elif arr[mid] > target:
        return binary_search(arr, left, mid-1, target)
    #case 3: Target is larget then search is RIGHT half
    else: 
        return binary_search(arr,mid+1,right,target)
