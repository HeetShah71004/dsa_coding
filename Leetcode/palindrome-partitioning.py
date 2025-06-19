from typing import List

class Solution:
    def isPalin(self, s: str) -> bool:
        return s == s[::-1]
    
    def getAllParts(self, s: str, partitions: List[str], ans: List[List[str]]):
        if len(s) == 0:
            ans.append(partitions.copy())
            return

        for i in range(len(s)):
            part = s[:i+1]
            if self.isPalin(part):
                partitions.append(part)
                self.getAllParts(s[i+1:], partitions, ans)
                partitions.pop()
    
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        partitions = []
        self.getAllParts(s, partitions, ans)
        return ans

# Create instance
sol = Solution()

# Example 1
s1 = "aab"
print("Example 1 Output:", sol.partition(s1))  
# Expected: [["a", "a", "b"], ["aa", "b"]]

# Example 2
s2 = "a"
print("Example 2 Output:", sol.partition(s2))  
# Expected: [["a"]]
