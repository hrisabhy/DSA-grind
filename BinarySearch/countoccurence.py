# Bruteforce approach using linear search
def brute(arr, n, k):
    count = 0
    for i in range(n):
        if arr[i] == k:
            count += 1
    return count


# Optimal approach using binary search
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


def firstandlast(arr, n, k):
    first = first_occurence(arr, n, k)
    if first == -1:
        return (-1, -1)
    last = last_occurence(arr, n, k)
    return (first, last)


def count_occurence(arr, n, k):
    first, last = firstandlast(arr, n, k)
    count = last - first + 1
    return count


arr = [2, 4, 6, 8, 8, 8, 11, 13]
n = len(arr)
k = 8
print(count_occurence(arr, n, k))
