from typing import List

def rearrange_bruteforce(nums: List[int]) -> List[int]:
    """
    Brute-force approach to rearrange elements with opposite signs in the array.
    
    Time Complexity: O(n)
    - Two passes through the array to separate positive and negative numbers.
    - One pass to construct the result array.

    Space Complexity: O(n)
    - Two separate arrays to store positive and negative numbers.
    """    
    n = len(nums)
    pos_arr = []
    neg_arr = []

    for i in range(n):
        if nums[i] > 0:
            pos_arr.append(nums[i])
        else:
            neg_arr.append(nums[i])

    for i in range(len(pos_arr)):
        nums[2 * i] = pos_arr[i]

    for i in range(len(neg_arr)):
        nums[2 * i + 1] = neg_arr[i]

    return nums

def rearrange_optimal(nums: List[int]) -> List[int]:
    """
    Optimal approach to rearrange elements with opposite signs in the array.
    
    Time Complexity: O(n)
    - Single pass through the array to rearrange elements.

    Space Complexity: O(1)
    - Constant space used for variables (pos_ind, neg_ind).
    """    
    n = len(nums)
    pos_ind = 0
    neg_ind = 1
    res_arr = [0] * n

    for i in range(n):
        if nums[i] > 0:
            res_arr[pos_ind] = nums[i]
            pos_ind += 2
        else:
            res_arr[neg_ind] = nums[i]
            neg_ind += 2
    
    return res_arr

nums = [3,1,-2,-5,2,-4]

# Test Brute-force Approach
result_bruteforce = rearrange_bruteforce(nums.copy())
print("Brute-force Result:", result_bruteforce)

# Test Optimal Approach
result_optimal = rearrange_optimal(nums.copy())
print("Optimal Result:", result_optimal)
print(result_bruteforce == result_optimal)