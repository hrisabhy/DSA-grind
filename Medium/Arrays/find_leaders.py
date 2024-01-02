def find_learders_bruteforce(arr):
    """
    Brute-force approach to find leaders in an array.
    
    Time Complexity: O(N^2)
    Space Complexity: O(1)
    """
    leaders = []
    n = len(arr)
    for i in range(n):
        leader_bol = True
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                leader_bol = False
                break
        
        if leader_bol:
            leaders.append(arr[i])
    return leaders 

def find_learders_optimal(arr):
    """
    Optimal approach to find leaders in an array.
    
    Time Complexity: O(N)
    Space Complexity: O(1)
    
    """    
    leaders = []
    n = len(arr)
    max_element = arr[n - 1]
    leaders.append(max_element)

    for i in range(n - 2, -1, -1):
        if arr[i] > max_element:
            leaders.insert(0, arr[i])
            max_element = arr[i]

    return leaders

arr = [10, 22, 12, 3, 0, 6]
# Brute-force approach
result_bruteforce = find_learders_bruteforce(arr)
print("Leaders (Brute-force):", result_bruteforce)
# Optimal approach
result_optimal = find_learders_optimal(arr)
print("Leaders (Optimal):", result_optimal)