class Solution:
    def countGoodArrays(self, n: int, m: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        
        # Base case: array of length 1 with 0 adjacent equal pairs
        dp[1][0] = m
        
        for i in range(2, n + 1):
            for j in range(0, min(i, k + 1)):
                # If we extend with the same number (increase adjacent equal count)
                if j > 0:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - 1] * 1) % MOD
                # If we extend with a different number
                dp[i][j] = (dp[i][j] + dp[i - 1][j] * (m - 1)) % MOD
        
        return dp[n][k]
sol = Solution()
print(sol.countGoodArrays(3, 2, 1))  # Output: 4
print(sol.countGoodArrays(4, 2, 2))  # Output: 6
print(sol.countGoodArrays(5, 2, 0))  # Output: 2
