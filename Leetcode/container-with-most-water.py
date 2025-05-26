# 11. container-with-most-water

# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.

# Example 1:
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Example 2:
# Input: height = [1,1]
# Output: 1

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_water = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            ht = min(height[left], height[right])
            curr_water = width * ht
            max_water = max(max_water, curr_water)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Create an instance of the Solution class
sol = Solution()

# Example 1
height1 = [1,8,6,2,5,4,8,3,7]
print("Output for Example 1:", sol.maxArea(height1))  # Expected Output: 49

# Example 2
height2 = [1,1]
print("Output for Example 2:", sol.maxArea(height2))  # Expected Output: 1

