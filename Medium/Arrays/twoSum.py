from typing import List

def brute_force_two_sum(arr: List[int], target: int) -> str:
    """
    Brute-force solution for the twoSum problem using nested loops.

    Time Complexity: O(n^2) (quadratic)
    Space Complexity: O(1) (constant)
    """
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                return "Yes"
    return "No"


def hash_table_two_sum(arr: List[int], target: int) -> str:
    """
    Optimized solution for the twoSum problem using a hash table.

    Time Complexity: O(n) (linear)
    Space Complexity: O(n) (linear)
    """
    num_index = {}

    for i, num in enumerate(arr):
        complement = target - num

        if complement in num_index:
            return "Yes"

        num_index[num] = i

    return "No"


def two_pointer_two_sum(arr: List[int], target: int) -> str:
    """
    Efficient solution for the twoSum problem using the two-pointer technique.

    Time Complexity: O(n log n) due to the sorting step
    Space Complexity: O(1) (constant)
    """
    arr.sort()
    left, right = 0, len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return "Yes"
        elif current_sum < target:
            left += 1
        else:
            right -= 1

    return "No"


# Example usage:
arr = [2, 7, 11, 15]
target = 9

# Testing each function
print(brute_force_two_sum(arr, target))
print(hash_table_two_sum(arr, target))    
print(two_pointer_two_sum(arr, target))
