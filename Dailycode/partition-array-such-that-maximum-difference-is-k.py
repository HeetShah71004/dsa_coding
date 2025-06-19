from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums = sorted(list(set(nums)))  # Remove duplicates and sort
        ans = 1
        mn = nums[0]

        for num in nums[1:]:
            if num - mn > k:
                ans += 1
                mn = num

        return ans

# Test the solution with given examples
sol = Solution()

# Example 1
nums1 = [3, 6, 1, 2, 5]
k1 = 2
print("Example 1 Output:", sol.partitionArray(nums1, k1))  # Expected: 2

# Example 2
nums2 = [1, 2, 3]
k2 = 1
print("Example 2 Output:", sol.partitionArray(nums2, k2))  # Expected: 2

# Example 3
nums3 = [2, 2, 4, 5]
k3 = 0
print("Example 3 Output:", sol.partitionArray(nums3, k3))  # Expected: 3
