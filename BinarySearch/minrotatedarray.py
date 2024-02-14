def findMin(arr, n):
    high = n - 1
    low = 0
    ans = float("inf")
    while low <= high:
        mid = low + (high - low) // 2
        if arr[low] <= arr[high]:
            ans = min(ans, arr[low])
            break
        if arr[low] <= arr[mid]:
            ans = min(ans, arr[low])
            low = mid + 1
        else:
            ans = max(ans, arr[mid])
            high = mid - 1
    return ans


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    n = len(arr)
    ans = findMin(arr, n)
    print("The minimum element is:", ans)
