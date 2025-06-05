# 74. search-a-2d-matrix

# You are given an m x n integer matrix matrix with the following two properties:

# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the previous row.
# Given an integer target, return true if target is in matrix or false otherwise.

# You must write a solution in O(log(m * n)) time complexity.

# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Example 2:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false

class Solution:
    def searchInRow(self, matrix, target, row):  # O(log n)
        n = len(matrix[0])
        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

    def searchMatrix(self, matrix, target):  # O(log m + log n)
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1

        while top <= bottom:
            mid_row = top + (bottom - top) // 2

            if matrix[mid_row][0] <= target <= matrix[mid_row][n - 1]:
                return self.searchInRow(matrix, target, mid_row)
            elif target > matrix[mid_row][n - 1]:
                top = mid_row + 1
            else:
                bottom = mid_row - 1

        return False

sol = Solution()
matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 34
print(sol.searchMatrix(matrix, target))  # Output: True

matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]
target = 31
print(sol.searchMatrix(matrix, target))  # Output: False