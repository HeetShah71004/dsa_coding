class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        res = cur = 0
        for c in reversed(s):
            if c == '0': 
                res += 1
            else:
                if cur + (1 << res) <= k:
                    cur += 1 << res
                    res += 1
        return res


# --- Example Test Cases ---

sol = Solution()

# Example 1:
s1 = "1001010"
k1 = 5
# Expected Output: 5
# Explanation: Possible subsequences like "00010", "00100", "00101" are ≤ 5.
print("Example 1 Output:", sol.longestSubsequence(s1, k1))  # Output: 5

# Example 2:
s2 = "00101001"
k2 = 1
# Expected Output: 6
# Explanation: Longest valid subsequence is "000001", binary value = 1.
print("Example 2 Output:", sol.longestSubsequence(s2, k2))  # Output: 6
