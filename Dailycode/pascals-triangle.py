from typing import List

class Solution: 
    def generate(self, numRows: int) -> List[List[int]]: 
        a = [[]] * numRows 
        for i in range(numRows): 
            a[i] = [1] * (i + 1) 
            for j in range(1, i // 2 + 1): 
                a[i][j] = a[i][i - j] = a[i - 1][j - 1] + a[i - 1][j] 
        return a 

# Create an instance of the Solution class
solution = Solution()

# Example 1:
# Input: numRows = 5
# Output: [[1], [1,1], [1,2,1], [1,3,3,1], [1,4,6,4,1]]
print("Example 1 Output:", solution.generate(5))

# Example 2:
# Input: numRows = 1
# Output: [[1]]
print("Example 2 Output:", solution.generate(1))
