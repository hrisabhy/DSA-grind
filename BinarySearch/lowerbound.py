def lowerbound_brute(arr, num):
    n = len(arr)
    for i in range(n):
        if arr[i] >= num:
            return i
    return n 

def lowerbound_optimal(arr, num):
    n = len(arr)
    high = n - 1
    low = 0
    ans = n
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] >= num:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
arr = [3,5,8,15,19]
print(lowerbound_brute(arr, 9))
print(lowerbound_optimal(arr, 9))