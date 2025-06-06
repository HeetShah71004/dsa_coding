# 240. search-a-2d-matrix-ii

# Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.

# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false

class Solution:
    def searchMatrix(self, mat: list[list[int]], tar: int) -> bool:
        m, n = len(mat), len(mat[0])
        r, c = 0, n - 1

        while r < m and c >= 0:
            if tar == mat[r][c]:
                return True
            elif tar < mat[r][c]:
                c -= 1
            else:
                r += 1

        return False

sol = Solution()
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 5
print(sol.searchMatrix(matrix, target))  # Output: True

matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 20
print(sol.searchMatrix(matrix, target))  # Output: False
