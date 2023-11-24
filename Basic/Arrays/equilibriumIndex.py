# Brute force approach
def equilibriumIndex(arr):
    n = len(arr) 
    for i in range(n):
        sum_right = 0
        sum_left = 0
        for j in range(i):
            sum_left += arr[j]
        for j in range(i+1, n):
            sum_right += arr[j]
        if sum_right == sum_left and sum_right != 0:
            return i
    return -1
print(equilibriumIndex([1, 7, 3, 6, 5, 6]))

# Optimal appoarch using prefix sum
def equilibriumIndex2(arr):
    n = len(arr)
    
    # Calculate total sum
    total_sum = 0
    for i in arr:
        total_sum += i

    left_sum = 0
    for i in range(n):
        right_sum = total_sum - left_sum - arr[i]
        if right_sum == left_sum:
            return i
        left_sum += arr[i]
    return -1
print(equilibriumIndex([1, 7, 3, 6, 5, 6]))