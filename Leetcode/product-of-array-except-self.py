# 238.product-of-array-except-self

# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        ans = [1] * n

        # Prefix product
        for i in range(1, n):
            ans[i] = ans[i - 1] * nums[i - 1]
        
        # Suffix product
        suffix = 1
        for i in range(n - 2, -1, -1):
            suffix *= nums[i + 1]
            ans[i] *= suffix
        
        return ans

# Test cases
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 4]
print("Input:", nums1)
print("Output:", solution.productExceptSelf(nums1))  # Output: [24, 12, 8, 6]

# Example 2
nums2 = [-1, 1, 0, -3, 3]
print("\nInput:", nums2)
print("Output:", solution.productExceptSelf(nums2))  # Output: [0, 0, 9, 0, 0]

