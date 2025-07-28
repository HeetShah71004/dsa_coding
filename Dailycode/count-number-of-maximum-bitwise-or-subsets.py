from typing import List

class Solution:
    def backtrack(self, nums, index, currentOR, maxOR, count):
        if currentOR == maxOR:
            count[0] += 1
        
        for i in range(index, len(nums)):
            self.backtrack(nums, i + 1, currentOR | nums[i], maxOR, count)
    
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOR = 0
        
        # Step 1: Compute the maximum OR
        for num in nums:
            maxOR |= num
        
        count = [0]
        # Step 2: Backtrack to count the subsets
        self.backtrack(nums, 0, 0, maxOR, count)
        
        return count[0]

# --------------------------
# Example test cases
# --------------------------
solution = Solution()

# Example 1
nums1 = [3, 1]
print("Input:", nums1)
print("Expected Output: 2")
print("Actual Output:", solution.countMaxOrSubsets(nums1))
print()

# Example 2
nums2 = [2, 2, 2]
print("Input:", nums2)
print("Expected Output: 7")
print("Actual Output:", solution.countMaxOrSubsets(nums2))
print()

# Example 3
nums3 = [3, 2, 1, 5]
print("Input:", nums3)
print("Expected Output: 6")
print("Actual Output:", solution.countMaxOrSubsets(nums3))
