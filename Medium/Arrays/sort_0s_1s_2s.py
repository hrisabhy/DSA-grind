from typing import List

def merge_sort(arr: List[int]) -> None:
    """
    Brute-force approach using Merge Sort.
    
    Time Complexity: O(n log n) due to the merge sort
    Space Complexity: O(n) for additional space during the merge sort
    """
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr

def count_sort(arr: List[int]) -> List[int]:
    """
    Better approach using Counting Frequencies.
    
    Time Complexity: O(n) for counting frequencies and O(n) for list reconstruction
    Space Complexity: O(1) for the frequency hash (assuming fixed number of elements)
    """
    freq_hash = {0: 0, 1: 0, 2: 0}

    for num in arr:
        freq_hash[num] += 1

    sorted_arr = [key for key in freq_hash for _ in range(freq_hash[key])]
    return sorted_arr

def dutch_national_flag(arr: List[int]) -> None:
    """
    Optimal approach using Dutch National Flag Algorithm.
    
    Time Complexity: O(n) as it iterates through the array once
    Space Complexity: O(1) as it uses constant extra space
    """
    low, mid, high = 0, 0, len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

# Example usage:
arr = [2, 0, 2, 1, 1, 0]

# Brute-force approach
sorted_arr = merge_sort(arr.copy())
print("Brute-force:", sorted_arr)

# Better approach
print("Better:", count_sort(arr.copy()))

# Optimal approach
dutch_national_flag(arr)
print("Optimal:", arr)