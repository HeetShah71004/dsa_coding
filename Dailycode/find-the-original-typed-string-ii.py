class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod = 10**9 + 7

        # Step 1: Split the word into segments of repeated letters.
        segments = []
        count = 1
        for i in range(1, len(word)):
            if word[i] == word[i - 1]:
                count += 1
            else:
                segments.append(count)
                count = 1
        segments.append(count)  # adding the last group count.

        # Step 2: Calculate the total combinations 
        total_ways = 1
        for segment in segments:
            total_ways = (total_ways * segment) % mod

        if len(segments) >= k:
            return total_ways  # If number of groups >= k, all combinations are valid

        # Step 3: DP to count number of combinations with total length < k
        dp = [0] * k
        dp[0] = 1  # 1 way to make the length 0

        for segment in segments:
            new_dp = [0] * k
            window = 0
            for length in range(1, k):
                window += dp[length - 1]
                if length - segment - 1 >= 0:
                    window -= dp[length - segment - 1]
                window %= mod
                new_dp[length] = window
            dp = new_dp

        # Total invalid = sum of dp[0 to k-1]
        invalid_ways = sum(dp) % mod

        return (total_ways - invalid_ways + mod) % mod


# ---------- Test Cases ----------

sol = Solution()

# Example 1
word1 = "aabbccdd"
k1 = 7
print("Example 1 Output:", sol.possibleStringCount(word1, k1))  # Expected: 5

# Example 2
word2 = "aabbccdd"
k2 = 8
print("Example 2 Output:", sol.possibleStringCount(word2, k2))  # Expected: 1

# Example 3
word3 = "aaabbb"
k3 = 3
print("Example 3 Output:", sol.possibleStringCount(word3, k3))  # Expected: 8
