def check_sorted(arr):
    sortFlag = True
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            sortFlag = False
    return sortFlag
print(check_sorted([1, 6, 3]))