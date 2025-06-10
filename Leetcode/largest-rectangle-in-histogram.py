# 84. largest-rectangle-in-histogram

# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.Input: heights = [2,1,5,6,2,3]

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Example 2:
# Input: heights = [2,4]
# Output: 4

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left = [0] * n   # index of nearest smaller to the left
        right = [0] * n  # index of nearest smaller to the right
        stack = []

        # Right smaller
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = n if not stack else stack[-1]
            stack.append(i)

        stack.clear()

        # Left smaller
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = -1 if not stack else stack[-1]
            stack.append(i)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            area = heights[i] * width
            max_area = max(max_area, area)

        return max_area 

sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3]))  # Output: 10
print(sol.largestRectangleArea([2,4]))  # Output: 4