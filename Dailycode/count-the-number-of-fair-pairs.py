class Solution:
    def countFairPairs(self, nums, lower, upper):
        nums.sort()

        left = 0
        right = len(nums) - 1
        count_within_upper = 0
        
        while left < right:
            if nums[left] + nums[right] <= upper:
                count_within_upper += (right - left)
                left += 1  # Move left pointer to the right since we've counted all valid pairs with `nums[left]`.
            else:
                right -= 1

        left = 0
        right = len(nums) - 1
        count_below_lower = 0
        
        while left < right:
            if nums[left] + nums[right] < lower:
                count_below_lower += (right - left)
                left += 1  # Move left pointer to the right since we've counted all valid pairs with `nums[left]`.
            else:
                right -= 1        
        return count_within_upper - count_below_lower

# Test cases
nums = [0,1,7,4,4,5] 
lower = 3 
upper = 6

solution = Solution()
result = solution.countFairPairs(nums, lower, upper)
print(result)  # Expected output: 6