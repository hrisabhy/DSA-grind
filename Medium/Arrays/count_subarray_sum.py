def subarraySum_brute(arr, target):
    """
    Time Complexity: O(N2), where N = size of the array.
    Reason: We are using two nested loops here. Though all are not running for exactly N times, the time complexity will be approximately O(N2).
    Space Complexity: O(1) as we are not using any extra space.
    """
    n = len(arr)
    count = 0
    for start in range(n):
        for end in range(start, n):
            if sum(arr[start : end + 1]) == target:
                count += 1
    return count


def subarraySum_optimal(arr, target):
    """
    Time Complexity: O(N) or O(N*logN) depending on which map data structure we are using, where N = size of the array.
    Space Complexity: O(N) as we are using a map data structure.
    """
    n = len(arr)
    count = 0
    prefix_sum = 0
    hash_map = {}
    hash_map[0] = 1
    for i in range(n):
        prefix_sum += arr[i]
        remove = prefix_sum - target
        count += hash_map.get(remove, 0)
        if prefix_sum in hash_map:
            hash_map[prefix_sum] += 1
        else:
            hash_map[prefix_sum] = 1
    return count


print(subarraySum_brute([3, 1, 2, 4], 6))
print(subarraySum_optimal([3, 1, 2, 4], 6))
