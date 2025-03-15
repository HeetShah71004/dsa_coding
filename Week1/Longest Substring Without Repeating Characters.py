# Approach  - Set

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxLength = 0
        charSet = set()
        left = 0
        
        for right in range(n):
            if s[right] not in charSet:
                charSet.add(s[right])
                maxLength = max(maxLength, right - left + 1)
            else:
                while s[right] in charSet:
                    charSet.remove(s[left])
                    left += 1
                charSet.add(s[right])
        
        return maxLength

# Test the solution
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))

print(s.lengthOfLongestSubstring("bbbbb"))

print(s.lengthOfLongestSubstring("pwwkew")) # 3

print(s.lengthOfLongestSubstring("dvdf")) # 3