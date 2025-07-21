from collections import defaultdict

class Solution:
    def makeFancyString(self, s: str) -> str:
        d = defaultdict(int)
        k = ''
        a = 0
        l = s[0]
        for i in s:
            if i == l:
                a += 1
                if a < 3:
                    k += i
            else:
                a = 1
                k += i
                l = i
        return k

# --- Test cases ---
sol = Solution()

# Example 1
s1 = "leeetcode"
print("Input:", s1)
print("Output:", sol.makeFancyString(s1))
print("Expected: leetcode\n")

# Example 2
s2 = "aaabaaaa"
print("Input:", s2)
print("Output:", sol.makeFancyString(s2))
print("Expected: aabaa\n")

# Example 3
s3 = "aab"
print("Input:", s3)
print("Output:", sol.makeFancyString(s3))
print("Expected: aab")
