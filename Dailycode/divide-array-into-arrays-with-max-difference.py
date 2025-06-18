from typing import List

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        ans = []
        for i in range(0, len(nums) - 2, 3):
            if nums[i + 2] - nums[i] > k:
                return []
            ans.append(nums[i:i + 3])
        return ans

# Test case 1
nums1 = [1, 3, 4, 8, 7, 9, 3, 5, 1]
k1 = 2
sol = Solution()
output1 = sol.divideArray(nums1, k1)
print("Output for Test Case 1:", output1)
# Expected: [[1,1,3],[3,4,5],[7,8,9]]

# Test case 2
nums2 = [2, 4, 2, 2, 5, 2]
k2 = 2
output2 = sol.divideArray(nums2, k2)
print("Output for Test Case 2:", output2)
# Expected: []
