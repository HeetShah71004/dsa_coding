from typing import List

class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        last = [-1] * 32
        for i in range(len(nums) - 1, -1, -1):
            for b in range(32):
                if nums[i] & (1 << b):
                    last[b] = i
            nums[i] = max(1, max(last) - i + 1)
        return nums

# Test examples
def main():
    sol = Solution()

    # Example 1
    nums1 = [1, 0, 2, 1, 3]
    print("Input:", nums1)
    result1 = sol.smallestSubarrays(nums1[:])  # Use nums1[:] to avoid modifying original
    print("Output:", result1)
    print("Expected: [3, 3, 2, 2, 1]")
    print()

    # Example 2
    nums2 = [1, 2]
    print("Input:", nums2)
    result2 = sol.smallestSubarrays(nums2[:])
    print("Output:", result2)
    print("Expected: [2, 1]")

if __name__ == "__main__":
    main()
