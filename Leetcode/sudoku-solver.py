# Write a program to solve a Sudoku puzzle by filling the empty cells.

# A sudoku solution must satisfy all of the following rules:

# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        def isSafe(board, row, col, dig):
            # Check row
            for j in range(9):
                if board[row][j] == dig:
                    return False
            
            # Check column
            for i in range(9):
                if board[i][col] == dig:
                    return False
            
            # Check 3x3 grid
            srow = (row // 3) * 3
            scol = (col // 3) * 3
            for i in range(srow, srow + 3):
                for j in range(scol, scol + 3):
                    if board[i][j] == dig:
                        return False
            return True

        def helper(board, row, col):
            if row == 9:
                return True
            
            nextRow, nextCol = row, col + 1
            if nextCol == 9:
                nextRow = row + 1
                nextCol = 0

            if board[row][col] != '.':
                return helper(board, nextRow, nextCol)

            for dig in map(str, range(1, 10)):
                if isSafe(board, row, col, dig):
                    board[row][col] = dig
                    if helper(board, nextRow, nextCol):
                        return True
                    board[row][col] = '.'
            return False

        helper(board, 0, 0)

board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

# Create object of Solution and solve
sol = Solution()
sol.solveSudoku(board)

# Print the solved board
for row in board:
    print(" ".join(row))
