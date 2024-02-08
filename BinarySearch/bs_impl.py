def binarySearchIterative(nums, target):
    n = len(nums)
    high = n - 1
    low = 0
    while low <= high:
        mid = (high + low) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1 # If target is not found

def binarySearchRecursive(nums, target, low, high):
    if low > high:
        return -1 # Base Case
    mid = (low + high) // 2
    if nums[mid] == target:
        return mid
    elif target > nums[mid]:
        return binarySearchRecursive(nums, target, mid + 1, high)
    return binarySearchRecursive(nums, target, low, mid - 1)

arr = [3, 4, 6, 7, 9, 12, 16, 17]
target = 6
print(binarySearchIterative(arr, target))
print(binarySearchRecursive(arr, target, 0, len(arr) - 1))