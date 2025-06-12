class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        
        # Find the shortest string in the array
        shortest = min(strs, key=len)
        
        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    return shortest[:i]
        
        return shortest

# Test cases
if __name__ == "__main__":
    solution = Solution()
    
    # Example 1
    strs1 = ["flower","flow","flight"]
    print(solution.longestCommonPrefix(strs1))  # Output: "fl"
    
    # Example 2
    strs2 = ["dog","racecar","car"]
    print(solution.longestCommonPrefix(strs2))  # Output: ""
    
    # Single string
    strs3 = ["alone"]
    print(solution.longestCommonPrefix(strs3))  # Output: "alone"
    
    # Empty list
    strs4 = []
    print(solution.longestCommonPrefix(strs4))  # Output: ""
    
    # Common prefix is the whole string
    strs5 = ["flower","flower","flower"]
    print(solution.longestCommonPrefix(strs5))  # Output: "flower"
    
    # No common prefix
    strs6 = ["abc","def","ghi"]
    print(solution.longestCommonPrefix(strs6))  # Output: ""
    
    # Common prefix with empty string in list
    strs7 = ["","flow","flight"]
    print(solution.longestCommonPrefix(strs7))  # Output: ""