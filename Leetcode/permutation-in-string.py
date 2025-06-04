# 567. permutation-in-string

# Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
# In other words, return true if one of s1's permutations is the substring of s2.

# Example 1:
# Input: s1 = "ab", s2 = "eidbaooo"
# Output: true
# Explanation: s2 contains one permutation of s1 ("ba").
# Example 2:
# Input: s1 = "ab", s2 = "eidboaoo"
# Output: false

class Solution:
    def isFreqSame(self, freq1, freq2):  # O(1)
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True

    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq = [0] * 26

        for ch in s1:
            freq[ord(ch) - ord('a')] += 1

        wind_size = len(s1)

        for i in range(len(s2) - wind_size + 1):
            wind_freq = [0] * 26
            for j in range(wind_size):
                wind_freq[ord(s2[i + j]) - ord('a')] += 1

            if self.isFreqSame(freq, wind_freq):
                return True

        return False

# Test cases
sol = Solution()

# Example 1
s1 = "ab"
s2 = "eidbaooo"
print(sol.checkInclusion(s1, s2))  # Output: True

# Example 2
s1 = "ab"
s2 = "eidboaoo"
print(sol.checkInclusion(s1, s2))  # Output: False