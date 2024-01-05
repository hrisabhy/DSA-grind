def printSpiral(matrix):
    """
    Time Complexity: O(m x n) { Since all the elements are being traversed once and there are total n x m elements ( m elements in each row and total n rows) so the time complexity will be O(n x m)}.
    Space Complexity: O(n) { Extra Space used for storing traversal in the ans array }.
    """
    top = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    left = 0

    result = []

    while top <= bottom and left <= right:
        # left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # right to left
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        # bottom to top
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result


print(printSpiral([[1, 2, 3, 4]]))
