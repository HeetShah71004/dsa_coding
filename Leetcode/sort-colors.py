# 75. sort-colors

# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
# You must solve this problem without using the library's sort function.

# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]

# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]

# Follow up: Could you come up with a one-pass algorithm using only constant extra space?

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:  # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1

nums = [2, 0, 2, 1, 1, 0]
Solution().sortColors(nums)
print(nums)  # Output: [0, 0, 1, 1, 2, 2]

# This version is in-place, O(n) time, and O(1) space, and is optimal for this problem.
