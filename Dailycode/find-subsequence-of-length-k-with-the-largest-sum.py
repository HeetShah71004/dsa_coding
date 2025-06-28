from typing import List

class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Pair each value with its original index
        indexed = [(val, idx) for idx, val in enumerate(nums)]

        # Step 2: Sort by value descending
        indexed.sort(key=lambda x: -x[0])

        # Step 3: Take top k values
        top_k = indexed[:k]

        # Step 4: Sort by original index to preserve order
        top_k.sort(key=lambda x: x[1])

        # Step 5: Extract the values
        return [val for val, _ in top_k]

# Test cases
sol = Solution()

# Example 1
nums1 = [2, 1, 3, 3]
k1 = 2
print("Example 1 Output:", sol.maxSubsequence(nums1, k1))  # Output: [3, 3]

# Example 2
nums2 = [-1, -2, 3, 4]
k2 = 3
print("Example 2 Output:", sol.maxSubsequence(nums2, k2))  # Output: [-1, 3, 4]

# Example 3
nums3 = [3, 4, 3, 3]
k3 = 2
print("Example 3 Output:", sol.maxSubsequence(nums3, k3))  # Output: [3, 4]
