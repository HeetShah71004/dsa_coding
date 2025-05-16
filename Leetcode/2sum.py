# 1.2sum
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

# Example 1:
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]

# Example 2:
# Input: nums = [3,2,4], target = 6
# Output: [1,2]

# Example 3:
# Input: nums = [3,3], target = 6
# Output: [0,1]

class Solution:
    def twoSum(self, nums, target):
        m = {}
        ans = []

        for i in range(len(nums)):
            first = nums[i]
            sec = target - first

            if sec in m:
                ans.append(i)
                ans.append(m[sec])
                break

            m[first] = i

        return ans

# Create an instance of the Solution class
sol = Solution()

# Test Case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print("Test Case 1 Output:", sol.twoSum(nums1, target1))  

# Test Case 2
nums2 = [3, 2, 4]
target2 = 6
print("Test Case 2 Output:", sol.twoSum(nums2, target2))  

# Test Case 3
nums3 = [3, 3]
target3 = 6
print("Test Case 3 Output:", sol.twoSum(nums3, target3)) 

