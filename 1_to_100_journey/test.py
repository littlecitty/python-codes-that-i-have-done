# 71. Implement binary search.

def binary_search(arr, left, right, target):
    # Base case: if range is invalid → target not found
    if left > right:
        return -1
    
    # Find the middle index
    mid = (left + right) // 2
    
    # Case 1: Target is exactly at mid
    if arr[mid] == target:
        return mid
    
    # Case 2: Target is smaller → search in LEFT half
    elif arr[mid] > target:
        return binary_search(arr, left, mid - 1, target)
    
    # Case 3: Target is larger → search in RIGHT half
    else:
        return binary_search(arr, mid + 1, right, target)


# Example usage
if __name__ == "__main__":
    numbers = [1, 3, 5, 7, 9, 11]
    target = int(input("enter an integer : "))
    result = binary_search(numbers, 0, len(numbers) - 1, target)
    
    if result != -1:
        print(f"Element {target} found at index {result}")
    else:
        print(f"Element {target} not found in the list")
