def linear_search(arr, target):
    # Your code here
    for i in range(0, len(arr)):
        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    for i, ele in enumerate(arr):
        if ele == target: 
            return i 
    
    return -1  # not found
