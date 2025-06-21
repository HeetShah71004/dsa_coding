from typing import List

class Solution:
    def helper(self, mat: List[List[int]], r: int, c: int, path: str, ans: List[str]):
        n = len(mat)
        # Check boundaries and invalid cells
        if r < 0 or c < 0 or r >= n or c >= n or mat[r][c] == 0 or mat[r][c] == -1:
            return
        
        # Reached destination
        if r == n - 1 and c == n - 1:
            ans.append(path)
            return
        
        # Mark current cell as visited
        mat[r][c] = -1
        
        # Explore all directions
        self.helper(mat, r + 1, c, path + "D", ans)  # Down
        self.helper(mat, r - 1, c, path + "U", ans)  # Up
        self.helper(mat, r, c - 1, path + "L", ans)  # Left
        self.helper(mat, r, c + 1, path + "R", ans)  # Right
        
        # Unmark current cell (backtrack)
        mat[r][c] = 1

    def findPath(self, mat: List[List[int]]) -> List[str]:
        n = len(mat)
        ans = []
        if mat[0][0] == 0 or mat[n-1][n-1] == 0:
            return ans  # No path possible if start or end blocked

        self.helper(mat, 0, 0, "", ans)
        return sorted(ans)  # Optional: sorted order


# Test Cases
sol = Solution()

# Test Case 1
mat1 = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 1]
]
print("Test Case 1 Output:", sol.findPath([row[:] for row in mat1]))  # ['DDRDRR', 'DRDDRR']

# Test Case 2
mat2 = [
    [1, 1],
    [1, 1]
]
print("Test Case 2 Output:", sol.findPath([row[:] for row in mat2]))  # ['DR', 'RD']

# Test Case 3 (No path)
mat3 = [
    [1, 0],
    [0, 1]
]
print("Test Case 3 Output:", sol.findPath([row[:] for row in mat3]))  # []

# Test Case 4 (Start or End blocked)
mat4 = [
    [0, 1],
    [1, 1]
]
print("Test Case 4 Output:", sol.findPath([row[:] for row in mat4]))  # []
