from typing import List

def max_subarray_sum_bruteforce(arr: List[int]) -> int:
    """
    Brute-force approach to find the contiguous subarray with the largest sum.
    
    Time Complexity: O(n^3)
    Space Complexity: O(1)
    """
    n = len(arr)
    max_sum = float("-inf")
    start, end = 0, 0

    # Iterate through all possible subarrays
    for i in range(n):
        for j in range(i, n):
            current_sum = sum(arr[i:j+1])
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    print("Maximum Sum Subarray:", arr[start:end+1])
    return max_sum

def max_subarray_sum_better(arr: List[int]) -> int:
    """
    Better approach using two nested loops to find the contiguous subarray with the largest sum.
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    n = len(arr)
    max_sum = float("-inf")
    start, end = 0, 0

    for i in range(n):
        current_sum = 0
        for j in range(i, n):
            current_sum += arr[j]
            if current_sum > max_sum:
                max_sum = current_sum
                start, end = i, j

    print("Maximum Sum Subarray:", arr[start:end+1])
    return max_sum

def max_subarray_sum_optimal(arr: List[int]) -> int:
    """
    Optimal approach using Kadane's algorithm to find the contiguous subarray with the largest sum.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    max_sum = float("-inf")
    current_sum = 0
    start, end = 0, 0

    for i in range(len(arr)):
        if current_sum + arr[i] < arr[i]:
            current_sum = arr[i]
            start = i
        else:
            current_sum += arr[i]

        if current_sum > max_sum:
            max_sum = current_sum
            end = i

    print("Maximum Sum Subarray:", arr[start:end+1])
    return max_sum

# Example usage:
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print("Brute-force Approach:", max_subarray_sum_bruteforce(arr))
print("Better Approach:", max_subarray_sum_better(arr))
print("Optimal Approach:", max_subarray_sum_optimal(arr))
