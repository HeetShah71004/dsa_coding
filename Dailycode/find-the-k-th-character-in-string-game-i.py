class Solution:
    def kthCharacter(self, k: int) -> str:
        s = "a"
        while len(s) < k:
            next_part = ''.join(chr(((ord(c) - ord('a') + 1) % 26) + ord('a')) for c in s)
            s += next_part
        return s[k - 1]

# Example 1
k1 = 5
sol = Solution()
output1 = sol.kthCharacter(k1)
print(f"Example 1:\nInput: k = {k1}\nOutput: \"{output1}\"\n")

# Example 2
k2 = 10
output2 = sol.kthCharacter(k2)
print(f"Example 2:\nInput: k = {k2}\nOutput: \"{output2}\"")
