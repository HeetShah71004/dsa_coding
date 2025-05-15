# 18. 4Sum

# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

# Example 2:
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ans = []
        n = len(nums)
        
        nums.sort()
        
        for i in range(n):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                p = j + 1
                q = n - 1
                while p < q:
                    curr_sum = nums[i] + nums[j] + nums[p] + nums[q]
                    
                    if curr_sum < target:
                        p += 1
                    elif curr_sum > target:
                        q -= 1
                    else:
                        ans.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1
                        
                        while p < q and nums[p] == nums[p-1]:
                            p += 1
        
        return ans

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    nums1 = [1, 0, -1, 0, -2, 2]
    target1 = 0
    result1 = solution.fourSum(nums1, target1)
    print("Test Case 1:")
    print("Input: nums =", nums1, ", target =", target1)
    print("Output:", result1)
    
    # Test Case 2
    nums2 = [2, 2, 2, 2, 2]
    target2 = 8
    result2 = solution.fourSum(nums2, target2)
    print("\nTest Case 2:")
    print("Input: nums =", nums2, ", target =", target2)
    print("Output:", result2)