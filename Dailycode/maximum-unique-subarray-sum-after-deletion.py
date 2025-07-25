from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        M = max(nums)
        if M <= 0:
            return M
        seen, Sum = 0, 0
        for x in nums:
            if x >= 0 and (seen >> x) & 1 == 0:
                Sum += x
                seen |= (1 << x)
        return Sum

# Test the function with provided examples
def main():
    sol = Solution()
    
    # Example 1
    nums1 = [1, 2, 3, 4, 5]
    print("Example 1 Output:", sol.maxSum(nums1))  # Expected: 15

    # Example 2
    nums2 = [1, 1, 0, 1, 1]
    print("Example 2 Output:", sol.maxSum(nums2))  # Expected: 1

    # Example 3
    nums3 = [1, 2, -1, -2, 1, 0, -1]
    print("Example 3 Output:", sol.maxSum(nums3))  # Expected: 3

if __name__ == "__main__":
    main()
