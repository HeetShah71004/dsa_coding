class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last_occurrence = {}
        
        for i, char in enumerate(s):
            last_occurrence[char] = i
        
        result = []
        start = 0
        end = 0
        
        for i, char in enumerate(s):
            end = max(end, last_occurrence[char])
            
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result

# Test cases

s = "ababcbacadefegdehijhklij"

solution = Solution()

print(solution.partitionLabels(s)) # Output: [9, 7, 8]