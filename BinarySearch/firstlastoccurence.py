# Bruteforce approach using linear search
def brute(arr, k):
    n = len(arr)
    first = -1
    last = -1
    for i in range(n):
        if arr[i] == k:
            if first == -1:
                first = i
            last = i
    return (first, last)


def upper_bound(arr, n, k):
    high = n - 1
    low = 0
    ans = n
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def lower_bound(arr, n, k):
    high = n - 1
    low = 0
    ans = n
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] >= k:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


# Better approach using lower and upper bound algorithm
def better(arr, n, k):
    lb = lower_bound(arr, n, k)
    if lb == n or arr[lb] != k:
        return (-1, -1)
    ub = upper_bound(arr, n, k)
    return (lb, ub - 1)


def first_occurence(arr, n, k):
    ans = -1
    high = n - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            ans = mid
            high = mid - 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return ans


def last_occurence(arr, n, k):
    ans = -1
    high = n - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == k:
            ans = mid
            low = mid + 1
        elif arr[mid] < k:
            low = mid + 1
        else:
            high = mid - 1
    return ans


# Optimal approach using binary search algorithm
def optimal(arr, n, k):
    first = first_occurence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = last_occurence(arr, n, k)
    return (first, last)


arr = [2, 4, 6, 8, 8, 8, 11, 13]
k = 8
print(optimal(arr, len(arr), k))
