def brute(arr):
    n = len(arr)
    for i in range(n):
        if (i == 0 or arr[i] > arr[i + 1]) and (i == n or arr[i] > arr[i - 1]):
            return i
    return -1


def optimal(arr):
    n = len(arr)
    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0
    if arr[n - 1] > arr[n - 2]:
        return n - 1
    low = 1
    high = n - 2
    while low <= high:
        mid = low + (high - low) // 2
        # if the mid index has the peak element
        if arr[mid] > arr[mid + 1] and arr[mid - 1] < arr[mid]:
            return mid
        # if we are on the left side
        if arr[mid] > arr[mid - 1]:
            low = mid + 1
        # if we are on the right side or if arr[mid] is the common point
        else:
            high = mid - 1
    return -1


print(optimal([1, 2, 3, 4, 5, 6, 7, 8, 5, 1]))
