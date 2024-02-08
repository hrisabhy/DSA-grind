def upperbound_brute(arr, num):
    n = len(arr)
    for i in range(n):
        if arr[i] > num:
            return i
    return n

def upperbound_optimal(arr, num):
    n = len(arr)
    high = n - 1
    low = 0
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] > num:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
arr = [3,5,8,9,15,19]
num = 9
print(upperbound_brute(arr, num))
print(upperbound_optimal(arr, num))