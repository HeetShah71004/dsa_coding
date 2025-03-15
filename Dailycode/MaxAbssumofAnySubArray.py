class Solution:
    def maxAbsoluteSum(self, nums):
        sum, minSum, maxSum = 0, 0, 0
        for num in nums:
            sum += num
            maxSum = max(maxSum, sum)
            minSum = min(minSum, sum)
        return abs(maxSum - minSum)

# Example usage
sol = Solution()
print(sol.maxAbsoluteSum([1,-3,2,3,-4])) # 5