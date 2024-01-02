from itertools import permutations

def next_permutation_bruteforce(arr):
    """
    Brute-force approach to find the lexicographically next greater permutation.
    
    Time Complexity: O(N!)
    Space Complexity: O(N!)

    """
    def generate_permutation(arr, start, result):
        if start == len(arr):
            result.append(arr.copy())
            return
        for i in range(start, len(arr)):
            arr[start], arr[i] = arr[i], arr[start]
            generate_permutation(arr, start+1, result)
            arr[start], arr[i] = arr[i], arr[start]
    
    result = []
    generate_permutation(arr, 0, result)

    result.sort()
    index = result.index(arr)

    if index == len(result) - 1:
        return result[0]
    else:
        return result[index + 1]

def next_permutation_better(arr):
    """
    Better approach using Python's built-in permutation function.
    
    Time Complexity: O(N! log(N))
    Space Complexity: O(N!)

    """    

    all_permutations = list(permutations(arr))

    # Find the next greater permutation
    all_permutations.sort()
    index = all_permutations.index(tuple(arr))

    # Return the next permutation or lowest possible order
    if index == len(all_permutations) - 1:
        return list(all_permutations[0])
    else:
        return list(all_permutations[index + 1])
    
def next_permutation_optimal(arr):
    """
    Optimal approach using breakpoint approach.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    
    """    
    # Step 1: Find the rightmost element smaller than its next element
    i = len(arr) - 2
    while i >= 0 and arr[i] > arr[i + 1]:
        i -= 1
    # If the array is in descending order, reverse it to get the lowest order
    if i == -1:
        arr.reverse()
        return arr
    # Step 2: Find the smallest element to the right of arr[i] that is greater than arr[i]
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1
    # Step 3: Swap arr[i] and arr[j]
    arr[i], arr[j] = arr[j], arr[i]
    # Step 4: Reverse the subarray to the right of arr[i]
    arr[i + 1:] = reversed(arr[i + 1:])

    return arr

# Example usage:
arr = [1, 3, 2]

# Brute-force approach
result_bruteforce = next_permutation_bruteforce(arr.copy())
print("Brute-force Approach:", result_bruteforce)

# Better approach
result_better = next_permutation_better(arr.copy())
print("Better Approach:", result_better)

# Optimal approach
result_optimal = next_permutation_optimal(arr.copy())
print("Optimal Approach:", result_optimal)