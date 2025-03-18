class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        max_length = 1
        
        left = 0
        used_bits = 0
        
        for right in range(n):
            while used_bits & nums[right] != 0:
                used_bits ^= nums[left]
                left += 1
                
            used_bits |= nums[right]
            
            max_length = max(max_length, right - left + 1)
            
        return max_length

# Test cases
nums = [1,3,8,48,10]
solution = Solution()

print(solution.longestNiceSubarray(nums)) # Output: 3