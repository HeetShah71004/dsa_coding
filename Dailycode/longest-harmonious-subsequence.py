class Solution:
    def findLHS(self, nums):
        from collections import Counter
        freq = Counter(nums)
        ans = 0
        for key in freq:
            if key + 1 in freq:
                ans = max(ans, freq[key] + freq[key + 1])
        return ans

# Test Cases
solution = Solution()

# Example 1
nums1 = [1, 3, 2, 2, 5, 2, 3, 7]
print("Example 1 Output:", solution.findLHS(nums1))  # Expected Output: 5

# Example 2
nums2 = [1, 2, 3, 4]
print("Example 2 Output:", solution.findLHS(nums2))  # Expected Output: 2

# Example 3
nums3 = [1, 1, 1, 1]
print("Example 3 Output:", solution.findLHS(nums3))  # Expected Output: 0
