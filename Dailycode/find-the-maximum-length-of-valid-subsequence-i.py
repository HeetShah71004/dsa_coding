from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 2:
            return 2
        z = nums[0] & 1  # Initial parity (0 for even, 1 for odd)
        Len = [1 - z, z, 1]  # Count of even, odd, and alternating
        for xx in nums[1:]:
            x = xx & 1
            Len[x & 1] += 1
            if x != z:
                Len[2] += 1
                z = 1 - z
        return max(Len)

# Test cases
sol = Solution()

# Example 1
nums1 = [1, 2, 3, 4]
print("Input:", nums1)
print("Output:", sol.maximumLength(nums1))  # Expected: 4

# Example 2
nums2 = [1, 2, 1, 1, 2, 1, 2]
print("\nInput:", nums2)
print("Output:", sol.maximumLength(nums2))  # Expected: 6

# Example 3
nums3 = [1, 3]
print("\nInput:", nums3)
print("Output:", sol.maximumLength(nums3))  # Expected: 2
