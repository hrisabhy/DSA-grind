from typing import List

def majority_element_bruteforce(arr: List[int]) -> int:
    """
    Brute-force approach to find the majority element.
    
    Time Complexity: O(n^2) due to nested loops
    Space Complexity: O(1)
    """
    n = len(arr)
    for i in range(n):
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        if count > n // 2:
            return arr[i]

def majority_element_hashmap(arr: List[int]) -> int:
    """
    Better approach using HashMap to find the majority element.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    element_count = {}
    n = len(arr)

    # Count occurrences of each element
    for num in arr:
        element_count[num] = element_count.get(num, 0) + 1

    # Find the element with more occurrences than n/2
    for key, value in element_count.items():
        if value > n // 2:
            return key

def majority_element_optimal(arr: List[int]) -> int:
    """
    Optimal approach using Moore's Voting Algorithm to find the majority element.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    candidate = None
    count = 0

    # Find the candidate for majority element
    for num in arr:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    # Verify if the candidate is the majority element
    count = 0
    for num in arr:
        if num == candidate:
            count += 1

    return candidate if count > len(arr) // 2 else None

# Example usage:
arr = [3, 3, 4, 2, 4, 4, 2, 4, 4]
print("Brute-force Approach:", majority_element_bruteforce(arr.copy()))
print("Better Approach:", majority_element_hashmap(arr.copy()))
print("Optimal Approach:", majority_element_optimal(arr.copy()))
