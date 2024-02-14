def findRotation(arr, n):
    high = n - 1
    low = 0
    ans = float("inf")
    index = -1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[low] <= arr[high]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            break
        elif arr[low] <= arr[mid]:
            if arr[low] < ans:
                ans = arr[low]
                index = low
            low = mid + 1
        else:
            if arr[mid] < ans:
                ans = arr[mid]
                index = mid
            high = mid - 1
    return index


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    n = len(arr)
    ans = findRotation(arr, n)
    print("The array is rotated", ans, "times.")
