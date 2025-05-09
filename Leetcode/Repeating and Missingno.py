# 2965. find-missing-and-repeated-values

# You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.

# Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.

# Example 1:

# Input: grid = [[1,3],[2,2]]
# Output: [2,4]
# Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4].

# Example 2:

# Input: grid = [[9,1,7],[8,9,2],[3,4,6]]
# Output: [9,5]
# Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        seen = set()
        n = len(grid)
        actual_sum = 0
        repeated = -1
    
        for i in range(n):
            for j in range(n):
                val = grid[i][j]
                actual_sum += val
                if val in seen:
                    repeated = val
                else:
                    seen.add(val)
        
        total_elements = n * n
        expected_sum = (total_elements * (total_elements + 1)) // 2
        missing = expected_sum - (actual_sum - repeated)

        return [repeated, missing]
    
# Test Cases
sol = Solution()

# Example 1
grid1 = [[1, 3], [2, 2]]
print("Test Case 1 Output:", sol.findMissingAndRepeatedValues(grid1))  # Expected: [2, 4]

# Example 2
grid2 = [[9, 1, 7], [8, 9, 2], [3, 4, 6]]
print("Test Case 2 Output:", sol.findMissingAndRepeatedValues(grid2))  # Expected: [9, 5]