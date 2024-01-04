def rotate_matrix_brute(matrix, n):
    """
    Time Complexity: O(N*N) to linearly iterate and put it into some other matrix.
    Space Complexity: O(N*N) to copy it into some other matrix.
    """
    rotated = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[i][j] = matrix[n - j - 1][i]
    return rotated

def rotate_matrix_optimal(matrix, n):
    """
    Time Complexity: O(N*N) + O(N*N).One O(N*N) is for transposing the matrix and the other is for reversing the matrix.
    Space Complexity: O(1).
    """
    # First find transpose of the matrix
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Reverse each row 
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(arr)
print(rotate_matrix_optimal(arr, n))