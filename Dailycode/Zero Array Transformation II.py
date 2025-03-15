class Solution:
    def minZeroArray(self, nums: list[int], queries: list[list[int]]) -> int:
        n = len(nums)
        
        def can_make_zero_array(k):
            diff = [0] * (n + 1)
            
            for i in range(k):
                left, right, val = queries[i]
                diff[left] += val
                diff[right + 1] -= val
            
            curr_val = 0
            for i in range(n):
                curr_val += diff[i]
                if curr_val < nums[i]:
                    return False
            
            return True
        
        if all(x == 0 for x in nums):
            return 0
        
        left, right = 1, len(queries)
        
        if not can_make_zero_array(right):
            return -1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if can_make_zero_array(mid):
                right = mid
            else:
                left = mid + 1
        
        return left

# Time complexity: O(n + q * log(q))
# Space complexity: O(n)

# nums = [1,2,3,4,5]
# queries = [[0,4,2],[-3,4,3],[-1,1,2],[0,2,3],[0,3,1]]
nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
print(Solution().minZeroArray(nums, queries))  

