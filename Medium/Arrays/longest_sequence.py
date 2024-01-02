def longest_sequence_brute(arr):
    """
    Naive approach to find the length of the longest consecutive sequence in an array.

    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    def linear_search(arr, element):
        for i in range(len(arr)):
            if arr[i] == element:
                return True
        return False
    
    longest = 1
    for i in range(len(arr)):
        x = arr[i]
        cnt = 1
        while linear_search(arr, x + 1):
            x += 1
            cnt += 1
        longest = max(longest, cnt)

    return longest

def longest_sequence_better(arr):
    """
    Time Complexity: O(N log N) due to sorting
    Space Complexity: O(1)
    """
    n = len(arr)
    if n == 0:
        return 0
    arr.sort()
    cnt = 0
    longest = 1
    last_smaller = float("-inf")
    for i in range(n):
        if arr[i] - 1 == last_smaller:
            cnt += 1
            last_smaller = arr[i]
        elif arr[i] != last_smaller:
            cnt = 1
            last_smaller = arr[i]
        longest = max(longest, cnt)
    
    return longest

def longest_sequence_optimal(arr):
    """
    Time Complexity: O(N)
    Space Complexity: O(N)
    """
    n = len(arr)
    longest = 1
    arr_set = set(arr)
    for element in arr_set:
        if element - 1 not in arr_set:
            cnt = 1
            x = element
            while x + 1 in arr_set:
                x += 1
                cnt += 1
            longest = max(longest, cnt)
    return longest

# Drive code
print(longest_sequence_optimal([100, 200, 1, 2, 3, 4]))
print(longest_sequence_brute([100, 200, 1, 2, 3, 4]))
print(longest_sequence_better([100, 200, 1, 2, 3, 4]))
