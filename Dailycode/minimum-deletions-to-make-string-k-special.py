from collections import Counter

class Solution:
    def minimumDeletions(self, word: str, k: int) -> int:
        m = Counter(word)
        va = list(m.values())
        ans = float('inf')
        
        for x in va:
            count = 0
            for y in va:
                if y < x:
                    count += y
                elif y > x + k:
                    count += y - x - k
            ans = min(ans, count)
        
        return ans


# Test cases
sol = Solution()

# Example 1
word1 = "aabcaba"
k1 = 0
print(f"Input: word = '{word1}', k = {k1}")
print(f"Output: {sol.minimumDeletions(word1, k1)}\n")  # Expected: 3

# Example 2
word2 = "dabdcbdcdcd"
k2 = 2
print(f"Input: word = '{word2}', k = {k2}")
print(f"Output: {sol.minimumDeletions(word2, k2)}\n")  # Expected: 2

# Example 3
word3 = "aaabaaa"
k3 = 2
print(f"Input: word = '{word3}', k = {k3}")
print(f"Output: {sol.minimumDeletions(word3, k3)}")  # Expected: 1
