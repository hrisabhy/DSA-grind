def search(arr, n, x):
    high = n - 1
    low = 0
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] == x:
            return True
        if arr[low] == arr[mid] and arr[mid] == high:
            low += 1
            high -= 1
            continue
        if arr[low] <= arr[mid]:
            if arr[low] <= x and x <= arr[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if arr[mid] <= x and x <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1
    return False


if __name__ == "__main__":
    arr = [7, 8, 1, 2, 3, 3, 3, 4, 5, 6]
    k = 3
    ans = search(arr, len(arr), k)
    if not ans:
        print("Target is not present.")
    else:
        print("Target is present in the array.")
