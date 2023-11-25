def firstMissing(arr):
    # find max
    max_int = float("-inf")
    for i in range(len(arr)):
        if arr[i] > max_int:
            max_int = arr[i]
    for i in range(1, max_int):
        if i not in arr:
            return i
        else:
            return max_int + 1
print(firstMissing([3, 2, -6, 1, 0]))