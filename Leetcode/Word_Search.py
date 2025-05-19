# 79.Word_Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false

class Solution:
    def exists(self, board, i, j, word, idx):
        if (i < 0 or i >= len(board) or 
            j < 0 or j >= len(board[0]) or 
            board[i][j] == '*' or 
            board[i][j] != word[idx]):
            return False
        
        if idx == len(word) - 1:
            return True
        
        ch = board[i][j]
        board[i][j] = '*'
        
        res = (self.exists(board, i + 1, j, word, idx + 1) or
               self.exists(board, i - 1, j, word, idx + 1) or
               self.exists(board, i, j + 1, word, idx + 1) or
               self.exists(board, i, j - 1, word, idx + 1))
        
        board[i][j] = ch
        return res

    def exist(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0] and self.exists(board, i, j, word, 0):
                    return True
        return False

sol = Solution()
board = [
    ['A','B','C','E'],
    ['S','F','C','S'],
    ['A','D','E','E']
]
word = "ABCCED"
print(sol.exist(board, word))  # Output: True
