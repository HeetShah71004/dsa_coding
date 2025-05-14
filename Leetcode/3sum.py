# 15. 3sum

# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]

# Example 2:
# Input: nums = [0,1,1]
# Output: []

class Solution(object):
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        ans = []

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue  # Skip duplicates for the first number

            j, k = i + 1, n - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total < 0:
                    j += 1
                elif total > 0:
                    k -= 1
                else:
                    ans.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for the second number
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1

        return ans

sol = Solution()
print(sol.threeSum([-1, 0, 1, 2, -1, -4])) # output: [[-1, -1, 2], [-1, 0, 1]]



