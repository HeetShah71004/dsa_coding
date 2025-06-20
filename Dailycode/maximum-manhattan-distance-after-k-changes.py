class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        ans = 0
        north = south = east = west = 0
        
        for i in range(len(s)):
            c = s[i]
            if c == 'N':
                north += 1
            elif c == 'S':
                south += 1
            elif c == 'E':
                east += 1
            elif c == 'W':
                west += 1
            
            x = abs(north - south)
            y = abs(east - west)
            MD = x + y
            dis = MD + min(2 * k, i + 1 - MD)
            ans = max(ans, dis)
        
        return ans

# Test cases
sol = Solution()

# Example 1
s1 = "NWSE"
k1 = 1
print("Example 1 Output:", sol.maxDistance(s1, k1))  # Expected: 3

# Example 2
s2 = "NSWWEW"
k2 = 3
print("Example 2 Output:", sol.maxDistance(s2, k2))  # Expected: 6
