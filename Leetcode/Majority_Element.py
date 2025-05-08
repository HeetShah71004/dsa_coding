# 169. majority-element

# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Example 1:

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        freq = 0
        ans = 0

        for num in nums:
            if freq == 0:
                ans = num
            if num == ans:
                freq += 1
            else:
                freq -=1
        
        count = 0
        for val in nums:
            if val == ans:
                count += 1
        if count > len(nums) // 2:
            return ans
        else:
            return -1 # This case shouldn't occur if majority element is guaranteed

# Create an instance of the Solution class
sol = Solution()

# Example 1
nums1 = [3, 2, 3]
print("Output:", sol.majorityElement(nums1))  # Expected Output: 3

# Example 2
nums2 = [2, 2, 1, 1, 1, 2, 2]
print("Output:", sol.majorityElement(nums2))  # Expected Output: 2
