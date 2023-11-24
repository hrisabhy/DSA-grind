def rotateArray(arr: list, k: int) -> list:
    temp = []
    for i in range(len(arr) - k):
        temp.append(arr[i+k])
    for j in range(k):
        temp.append(arr[j])
    return temp
print(rotateArray([1, 2, 3, 4, 5], 3))

# Better Approach 

def rotateArray2(arr: list[int], k: int):
    k = k % len(arr) # In case k > length of array
    # First reverse k elements
    reverse(arr, 0, k - 1)

    # Then reverse n - k elements
    reverse(arr, k, len(arr) - 1)

    # Then reverse the whole array
    reverse(arr, 0, len(arr) - 1)
    
    return arr

def reverse(arr: list[int], start: int, end: int):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr
print(rotateArray2([1, 2, 3, 4, 5], 3))