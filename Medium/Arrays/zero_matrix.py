def zero_matrix_brute(matrix, n, m):
    """
    Time Complexity: O((N*M)*(N + M)) + O(N*M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
    Space Complexity: O(1) as we are not using any extra space.

    """

    def swap_rows(matrix, m, i):
        for j in range(m):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    def swap_cols(matrix, n, j):
        for i in range(n):
            if matrix[i][j] != 0:
                matrix[i][j] = -1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                swap_rows(matrix, m, i)
                swap_cols(matrix, n, j)

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == -1:
                matrix[i][j] = 0

    return matrix


def zero_matrix_better(matrix, n, m):
    """
    Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
    Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

    Space Complexity: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.
    Reason: O(N) is for using the row array and O(M) is for using the col array.
    """
    rows = [0] * n
    cols = [0] * m

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                rows[i] = 1
                cols[j] = 1

    for i in range(n):
        for j in range(m):
            if rows[i] or cols[j]:
                matrix[i][j] = 0

    return matrix


def zero_matrix_optimal(matrix, n, m):
    """
    Time Complexity: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.
    Reason: In this approach, we are also traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

    Space Complexity: O(1) as we are not using any extra space.
    """
    col0 = 1
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                matrix[i][0] = 0

                if j != 0:
                    matrix[0][j] = 0
                else:
                    col0 = 0

    for i in range(1, n):
        for j in range(1, m):
            if matrix[i][j] != 0:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

    if matrix[0][0] == 0:
        for j in range(m):
            matrix[0][j] = 0
    if col0 == 0:
        for i in range(n):
            matrix[i][0] = 0
    return matrix
