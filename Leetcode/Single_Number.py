# 136. single-number

# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ans = 0
        for val in nums:
            ans ^= val  # XOR operation
        return ans

# Example test case
nums = [2, 2, 1]

# Creating an instance of the Solution class
sol = Solution()

# Calling the singleNumber method and printing the result
print(sol.singleNumber(nums))  # Output: 1
