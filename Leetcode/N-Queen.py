# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.

# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.

# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.

class Solution:
    def isSafe(self, board, row, col, n):
        # Check horizontal
        for j in range(n):
            if board[row][j] == 'Q':
                return False
        
        # Check vertical
        for i in range(n):
            if board[i][col] == 'Q':
                return False
        
        # Check left diagonal (upper left)
        i, j = row, col
        while i >= 0 and j >= 0:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j -= 1
        
        # Check right diagonal (upper right)
        i, j = row, col
        while i >= 0 and j < n:
            if board[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        
        return True
    
    def nQueens(self, board, row, n, ans):
        if row == n:
            ans.append(["".join(row) for row in board])
            return
        
        for j in range(n):
            if self.isSafe(board, row, j, n):
                board[row][j] = 'Q'
                self.nQueens(board, row + 1, n, ans)
                board[row][j] = '.'
    
    def solveNQueens(self, n: int) -> list[list[str]]:
        board = [['.' for _ in range(n)] for _ in range(n)]
        ans = []
        self.nQueens(board, 0, n, ans)
        return ans
    
# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test case 1: n = 4
    n1 = 4
    result1 = sol.solveNQueens(n1)
    print(f"Solutions for n = {n1}:")
    for soln in result1:
        for row in soln:
            print(row)
        print()

    # Test case 2: n = 1
    n2 = 1
    result2 = sol.solveNQueens(n2)
    print(f"Solutions for n = {n2}:")
    for soln in result2:
        for row in soln:
            print(row)
        print()