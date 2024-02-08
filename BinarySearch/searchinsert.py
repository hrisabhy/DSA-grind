def searchInsert(arr, num):
    n = len(arr)
    high = n - 1
    low = 0
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] >= num:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
print(searchInsert([1,2,4,7], 6))