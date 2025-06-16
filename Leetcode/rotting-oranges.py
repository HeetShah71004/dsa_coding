from collections import deque

class Solution:
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        # Step 1: Collect initial rotten oranges and count fresh ones
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))  # (row, col, time)
                elif grid[r][c] == 1:
                    fresh += 1
        
        # Directions: up, down, left, right
        directions = [(-1,0), (1,0), (0,-1), (0,1)]
        time_elapsed = 0

        # Step 2: BFS traversal to rot adjacent fresh oranges
        while queue:
            r, c, time_elapsed = queue.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    fresh -= 1
                    queue.append((nr, nc, time_elapsed + 1))
        
        # Step 3: Check if all fresh oranges have been rotted
        return time_elapsed if fresh == 0 else -1

sol = Solution()
print(sol.orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # Output: 4
print(sol.orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # Output: -1
print(sol.orangesRotting([[0,2]]))                   # Output: 0
